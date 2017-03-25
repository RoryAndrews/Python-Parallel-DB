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
        pass
