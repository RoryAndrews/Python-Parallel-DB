import sys
import re

from antlr4 import *
from antlr4.InputStream import InputStream

from lib import ConnectionLoader

from lib.MySQL.MySQLLexer import MySQLLexer
from lib.MySQL.MySQLListener import MySQLListener
from lib.MySQL.MySQLParser import MySQLParser
from lib.MySQL.MySQLLoader import MySQLLoader

def processSQL(sqlfilename):
    try:
        # Use antlr4 to parse sqlfile
        sql_input = FileStream(sqlfilename)
        sql_lexer = MySQLLexer(sql_input)
        sql_lexer.removeErrorListeners()
        sql_stream = CommonTokenStream(sql_lexer)
        sql_parser = MySQLParser(sql_stream)
        sql_tree = sql_parser.statement()

        sql_loader = MySQLLoader()
        walker = ParseTreeWalker()
        walker.walk(sql_loader, sql_tree)

        return (sql_loader.sqltype, sql_loader.aliases, sql_loader.columns, sql_loader.comparisons)
    except BaseException as e:
        print(str(e))
        return (None, None, None, None)

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

    print(processSQL(sqlfilename))
