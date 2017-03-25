import threading
import mysql.connector.pooling
import re


class PartitionJoinThread (threading.Thread):
    def __init__(self, threadID, plan, tableM, tableM_connection, tableN, tableN_connection, columns, partitionedsql, sqlfilename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.plan = plan
        self.temp_tablename = None
        self.tableM = tableM
        self.tableM_connection = tableM_connection
        self.tableN = tableN
        self.tableN_connection = tableN_connection
        self.columns = columns
        self.partitionedsql = partitionedsql
        self.sqlfilename = sqlfilename

    def run(self):
        transfer = self.plan[1]
        if transfer != 0:
            self.__transfer()

        cursor = self.tableM_connection.cursor()

        if transfer <= 0:
            cursor = self.tableM_connection.cursor()
        else:
            cursor = self.tableN_connection.cursor()

        sqlstatement = self.__generateSQL()

        cursor.execute(sqlstatement)
        results = cursor.fetchall()

        for row in results:
            print(*row, sep=' | ')

    def __generateSQL(self):
        transfer = self.plan[1]

        if transfer == 0:
            return self.partitionedsql.format(self.tableM, self.tableN)
        elif transfer > 0:
            return self.partitionedsql.format(self.temp_tablename, self.tableN)
        else:
            return self.partitionedsql.format(self.tableM, self.temp_tablename)

    def __transfer(self):
        if self.plan[1] < 0:
            out_table = self.tableN
            out_conn = self.tableN_connection
            in_table = self.tableM
            in_conn = self.tableM_connection
            self.temp_tablename = "_TEMP_" + self.tableN + "" + str(self.plan[0][1] + 1)
        else:
            out_table = self.tableM
            out_conn = self.tableM_connection
            in_table = self.tableN
            in_conn = self.tableN_connection
            self.temp_tablename = "_TEMP_" + self.tableM + "" + str(self.plan[0][0] + 1)

        transferquery = "SELECT "
        for info in self.columns:
            table = info[0]
            column = info[1]
            if table == out_table:
                transferquery += column + ", "
        transferquery = transferquery[:-2] # to remove final ", "
        transferquery += " FROM " + out_table + ";"

        out_cursor = out_conn.cursor(buffered=True)
        in_cursor = in_conn.cursor(buffered=True)

        out_cursor.execute(transferquery)
        results = out_cursor.fetchall()
        column_description = out_cursor.column_names
        out_cursor.execute("DESCRIBE {};".format(out_table))
        description = out_cursor.fetchall()

        create_temp_table = "CREATE TEMPORARY TABLE " + self.temp_tablename
        create_temp_table += " ("
        for column in column_description:
            datatype = self.__getDataType(column, description)
            create_temp_table += column + " " + datatype + ", "
        create_temp_table = create_temp_table[:-2] # to remove final ", "
        create_temp_table += ");"

        in_cursor.execute(create_temp_table)

        insert_statement = "INSERT INTO {} (".format(self.temp_tablename)
        for column in column_description:
            insert_statement += column + ", " # Adding each column name in.
        insert_statement = insert_statement[:-2] # to remove final ", "
        insert_statement += ") VALUES ("
        for i in column_description:
            insert_statement += "%s, "
        insert_statement = insert_statement[:-2] # to remove final ", "
        insert_statement += ")"

        in_cursor.executemany(insert_statement, results)
        in_cursor.close()
        out_cursor.close()
        in_conn.commit()

    def __getDataType(self, column, description):
        for info in description:
            if column == info[0]:
                return info[1]
        return "varchar(128)"
