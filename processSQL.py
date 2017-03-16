import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQL.MySQLLexer import MySQLLexer
from lib.MySQL.MySQLListener import MySQLListener
from lib.MySQL.MySQLParser import MySQLParser

from lib.SQLLoader import SQLLoader
from lib import catdb
from lib import ConnectionLoader

def processSQL(cataloginfo, numnodes, nodeinfo, sqlfilename):
    conn_list = None

    meta_catalog = catdb.getCatalogParams(cataloginfo)

    # print(meta_catalog)
    sql_input = FileStream(sqlfilename)
    sql_lexer = MySQLLexer(sql_input)
    sql_stream = CommonTokenStream(sql_lexer)
    sql_parser = MySQLParser(sql_stream)
    sql_tree = sql_parser.statement()

    sql_loader = SQLLoader()
    walker = ParseTreeWalker()
    walker.walk(sql_loader, sql_tree)
    print(sql_loader.sql)

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
