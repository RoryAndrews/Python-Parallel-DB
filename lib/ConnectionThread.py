import threading
import mysql.connector
import catdb
import re

# Allows multithreading when creating a connection to database and executing a ddl.
class ConnectionThread (threading.Thread):
    def __init__(self, threadID, catalogconn, nodeconn, sqlstatement, sqlstatement_name, dtablerow=None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.catalogconn = catalogconn
        self.nodeconn = nodeconn
        self.sqlstatement = sqlstatement
        self.sqlstatement_name = sqlstatement_name
        self.dtablerow = dtablerow

    def run(self):
        try:
            cursor = self.nodeconn.cursor()
            self.nodeconn.start_transaction()
            # If create table then execute and update catalog.
            if re.search("CREATE TABLE", self.sqlstatement, flags=re.IGNORECASE | re.MULTILINE):
                cursor.execute(self.sqlstatement)
                result = catdb.insertTable(self.catalogconn, self.dtablerow) # Updates dtables
                if result:
                    self.nodeconn.commit()
                else:
                    self.nodeconn.rollback()
            elif re.search("DROP TABLE", self.sqlstatement, flags=re.IGNORECASE | re.MULTILINE) and dtablerow:
                cursor.execute(self.sqlstatement)
                result = catdb.removeByTable(self.catalogconn, self.dtablerow) # Updates dtables
                if result:
                    self.nodeconn.commit()
                else:
                    self.nodeconn.rollback()
            else
                cursor.execute(self.sqlstatement)
                self.nodeconn.commit()

            print("[{}:{}/{}]: {} success".format(self.nodeconn.host, self.nodeconn.port, self.nodeconn.database, self.sqlstatement_name))
        except mysql.connector.Error as err:
            print("[{}:{}/{}]: {} failure".format(self.nodeconn.host, self.nodeconn.port, self.nodeconn.database, self.sqlstatement_name))
            print("SQL ERROR: {}".format(err.msg))
        finally:
            cursor.close()
            self.nodeconn.close()


if __name__ == "__main__":
    clustercfg = {
        'hostname': "jdbc:db2://127.0.0.1:3306/testdb",
        'username': "dbuser",
        'passwd': "mypasswd"
    }

    sqlstatement1 = "CREATE TABLE BOOKS(isbn char(14), title char(80), price decimal);"
    sqlstatement2 = "DROP TABLE BOOKS;"


    dtablerow = {
        'tname': "BOOKS",
        'nodedriver': "test",
        'nodeurl': "jdbc:db2://127.0.0.1:3306/testdb",
        'nodeuser': "dbuser",
        'nodepasswd': "mypasswd",
        'partmtd': None,
        'nodeid': 1,
        'partcol': None,
        'partparam1': None,
        'partparam2': None
    }

    cparams = catdb.getCatalogParams(clustercfg)

    connection = mysql.connector.connect(**cparams)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS DTABLES;")
    cursor.execute("DROP TABLE IF EXISTS BOOKS;")
    cursor.close()
    connection.close()

    cnxpool = mysql.connector.connect(pool_name = "cnxpool", pool_size = "5", **cparams)

    catdb.makeDtables(cnxpool.get_connection())

    input("Press Enter to create table")

    thread = ConnectionThread(dtablerow['nodeid'], cnxpool.get_connection(), cnxpool.get_connection(), sqlstatement1, dtablerow)
    thread.run()

    input("Press Enter to drop table")

    thread = ConnectionThread(dtablerow['nodeid'], cnxpool.get_connection(), cnxpool.get_connection(), sqlstatement2, dtablerow)