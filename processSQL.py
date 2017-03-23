import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib import ConnectionLoader

from lib.MySQL.MySQLLexer import MySQLLexer
from lib.MySQL.MySQLListener import MySQLListener
from lib.MySQL.MySQLParser import MySQLParser
from lib.SQLLoader import SQLLoader

def processSQL(cataloginfo, numnodes, nodeinfo, sqlfilename):
    #Use antlr4 to parse sqlfile
    sql_input = FileStream(sqlfilename)
    sql_lexer = MySQLLexer(sql_input)
    sql_stream = CommonTokenStream(sql_lexer)
    sql_parser = MySQLParser(sql_stream)
    # sql_tree = sql_parser.statement()
    sql_tree = sql_parser.statement()


    sql_loader = SQLLoader()
    walker = ParseTreeWalker()
    walker.walk(sql_loader, sql_tree)
    print(sql_loader.where)
    print (sql_loader.select)
    print (sql_loader.alias)
    # 
    # print (sql_loader.test)
    #print (cataloginfo, numnodes, nodeinfo, sqlfilename)

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

    processSQL(catalog,numnodes,nodeinfo,sqlfilename)
