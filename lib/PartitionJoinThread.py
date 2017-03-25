import threading
import mysql.connector.pooling
import re


class PartitionJoinThread (threading.Thread):
    def __init__(self, threadID, plan, tableM, tableM_connection, tableN, tableN_connection, columns, partitionedsql, sqlfilename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.plan = plan
        self.tableM = tableM
        self.tableM_connection = tableM_connection
        self.tableN = tableN
        self.tableN_connection = tableN_connection
        self.columns = columns
        self.partitionedsql = partitionedsql
        self.sqlfilename = sqlfilename

    def run(self):
        if self.plan[1] != 0:
            self.__transfer()

    def __transfer(self):
        if self.plan[1] < 0:
            out_table = self.tableN
            out_conn = self.tableN_connection
            in_table = self.tableM
            in_conn = self.tableM_connection
        else:
            out_table = self.tableM
            out_conn = self.tableM_connection
            in_table = self.tableN
            in_conn = self.tableN_connection


        transferquery = "SELECT "
        for info in self.columns:
            table = info[0]
            column = info[1]
            print(table, column)
            if table == out_table:
                transferquery += column + ", "
        transferquery = transferquery[:-2] # to remove final ", "
        transferquery += " FROM " + out_table + ";"

        print(transferquery)

        out_cursor = out_conn.cursor()
        in_cursor = in_conn.cursor()

        out_cursor.execute(transferquery)
        print(out_cursor.fetchall())
