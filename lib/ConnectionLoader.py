import mysql.connector
import re

if __name__ == "__main__":
    import catdb
else:
    from lib import catdb

class ConnectionLoader(object):
    def __init__(self, catalogconn, nodeconn, tableinfo, data):
        self.nodeconn = nodeconn
        self.catalogconn = catalogconn
        self.tableinfo = tableinfo
        self.data = data

    def loadData(self):
        try:
            self.nodeconn.start_transaction()
            cursor = self.nodeconn.cursor(buffered=True)
            
            # Get column names
            cursor.execute("SELECT * FROM {};".format(self.tableinfo['tname']))
            fieldnames = [i[0] for i in cursor.description]

            # Generate insert statement
            insert_statement = "INSERT INTO {} (".format(self.tableinfo['tname'])
            for col in fieldnames:
                insert_statement += col + ", " # Adding each column name in.
            insert_statement = insert_statement[:-2] # to remove final ", "
            insert_statement += ") VALUES ("
            for i in fieldnames:
                insert_statement += "%s, "
            insert_statement = insert_statement[:-2] # to remove final ", "
            insert_statement += ")"

            # print("insert_statement:\n{}".format(insert_statement)) # COMMENT OUT
            # print(self.data) # COMMENT OUT

            cursor.executemany(insert_statement, self.data)
        except mysql.connector.Error as err:
            print("ERROR: Loading with node{}:\ntableinfo: {}".format(self.tableinfo['nodeid'], self.tableinfo))
            print(err)
        except BaseException as e:
            print("Failed to load data with node{}:\ntableinfo: {}".format(self.tableinfo['nodeid'], self.tableinfo))
            print(str(e))
        finally:
            cursor.close()

    def commit(self):
        if self.nodeconn:
            self.nodeconn.commit()
            self.nodeconn.close()
            result = catdb.partitionUpdate(self.catalogconn, self.tableinfo)
            if not result:
                print("Error updating catalog.\ntableinfo: {}".format(self.tableinfo))
        else:
            print("Commit Error: No connection remaining.\ntableinfo: {}".format(self.tableinfo))

    def rollback(self):
        if self.nodeconn:
            self.nodeconn.rollback()
            self.nodeconn.close()
        else:
            print("Rollback Error: No connection remaining.\ntableinfo: {}".format(self.tableinfo))
