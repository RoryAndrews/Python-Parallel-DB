import threading
import mysql.connector.pooling
import re

if __name__ == "__main__":
    import catdb
else:
    from lib import catdb

# Allows multithreading when creating a connection to database and executing an SQL statement.
# threadID: a number representing this unique thread.
# catalogconn: a mysql connection for the catalog.
# nodeconn: a mysql connection for the node to be executed on.
# sqlstatement: the exact SQL statement that will be executed on the node.
# sqlstatement_name: used for error message.
# dtablerow: A dictionary with keys matching the columns in DTABLES.
#   dtablerow must contain values for the following keys depending on the sql statement:
#       CREATE TABLE: tname, nodedriver, nodeurl, nodeuser, nodepasswd, nodeid
#       DROP TABLE: tname
#       PARTITION UPDATE (using csvLoader): tname, partmtd, partcol, partparam1, partparam2, nodeid
#       OTHER: dtablerow is not needed.
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
        success = False
        try:
            cursor = self.nodeconn.cursor()
            self.nodeconn.start_transaction()
            # If create table then execute and update catalog.
            if re.search("CREATE TABLE", self.sqlstatement, flags=re.IGNORECASE | re.MULTILINE):
                cursor.execute(self.sqlstatement)
                result = catdb.insertTable(self.catalogconn, self.dtablerow) # Updates dtables
                if result:
                    self.nodeconn.commit()
                    success = True
                else:
                    print("Rolling back transaction for thread {}".format(self.threadID))
                    self.nodeconn.rollback()
            elif re.search("DROP TABLE", self.sqlstatement, flags=re.IGNORECASE | re.MULTILINE) and dtablerow:
                cursor.execute(self.sqlstatement)
                result = catdb.removeByTable(self.catalogconn, self.dtablerow) # Updates dtables
                if result:
                    self.nodeconn.commit()
                    success = True
                else:
                    print("Rolling back transaction for thread {}".format(self.threadID))
                    self.nodeconn.rollback()
            else:
                cursor.execute(self.sqlstatement)
                self.nodeconn.commit()
                success = True
        except mysql.connector.Error as err:
                print("SQL ERROR: {}".format(err.msg))
        finally:
            if success:
                self.__printSuccess()
            else:
                self.__printFailure()
            cursor.close()
            self.nodeconn.close()

    def __printSuccess(self):
        if not self.sqlstatement_name:
            self.sqlstatement_name = 'sql'
        try:
            print("[{}:{}/{}]: {} success".format(self.nodeconn.server_host, self.nodeconn.server_port, self.nodeconn.database, self.sqlstatement_name))
        except:
            try:
                print("[{}]: {} success".format(self.dtablerow['nodeurl'], self.sqlstatement_name))
            except:
                print("THREAD {}: success".format(self.threadID))

    def __printFailure(self):
        if not self.sqlstatement_name:
            self.sqlstatement_name = 'sql'
        try:
            print("[{}:{}/{}]: {} failure".format(self.nodeconn.server_host, self.nodeconn.server_port, self.nodeconn.database, self.sqlstatement_name))
        except AttributeError:
            try:
                print("[{}]: {} failure".format(self.dtablerow['nodeurl'], self.sqlstatement_name))
            except:
                print("THREAD {}: failure".format(self.threadID))


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

    cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cnxpool", pool_size = 6, **cparams)

    catdb.makeDtables(cnxpool.get_connection())

    input("Press Enter to create table")
    thread = ConnectionThread(dtablerow['nodeid'], cnxpool.get_connection(), cnxpool.get_connection(), sqlstatement1, "sqlstatement1", dtablerow)
    thread.run()

    input("Press Enter to drop table")

    thread = ConnectionThread(dtablerow['nodeid'], cnxpool.get_connection(), cnxpool.get_connection(), sqlstatement2, "sqlstatement2", dtablerow)
    thread.run()
