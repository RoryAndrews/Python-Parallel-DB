import sys
import re

from antlr4 import *
from antlr4.InputStream import InputStream

from lib import ConnectionLoader

from lib.MySQL.MySQLLexer import MySQLLexer
from lib.MySQL.MySQLListener import MySQLListener
from lib.MySQL.MySQLParser import MySQLParser
from lib.SQLLoader import SQLLoader

def processSQL(sqlfilename):
    # try:
        #Use antlr4 to parse sqlfile
        sql_input = FileStream(sqlfilename)
        sql_lexer = MySQLLexer(sql_input)
        sql_lexer.removeErrorListener(ConsoleErrorListener)
        sql_stream = CommonTokenStream(sql_lexer)
        sql_parser = MySQLParser(sql_stream)
        # sql_tree = sql_parser.statement()
        sql_tree = sql_parser.statement()


        sql_loader = SQLLoader()
        walker = ParseTreeWalker()
        walker.walk(sql_loader, sql_tree)

        column_list = set()
        for item in sql_loader.select:
            column_list.add(item)

        for item in sql_loader.where:
            m = re.search('^([\w\d]+).([\w\d])+$', item[0])
            (table, column) = m.group(1, 2)
            column_list.add((table, column))

        return (sql_loader.data, sql_loader.alias, column_list)
    # except:
    #     return (None, None, None)

if __name__ =="__main__":
    catalog = {
        'driver' : 'com.ibm.db2.jcc.DB2Driver',
        'hostname' : 'jdbc:db2://127.0.0.1:3306/testdb',
        'username' : 'dbuser',
        'passwd' : 'mypasswd',
    }

    numnodes = 2

    nodeinfo = {
        'nodeid' : '1',
        'driver' : 'com.ibm.db2.jcc.DB2Driver',
        'hostname' : 'jdbc:db2://127.0.0.1:3306/testdb',
        'username' : 'dbuser',
        'passwd' : 'mypasswd',
    }

    sqlfilename = "process_sqlfile"

    processSQL(sqlfilename)
