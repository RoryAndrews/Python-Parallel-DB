import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQL.MySQLParser import MySQLParser
from lib.MySQL.MySQLListener import MySQLListener

class SQLLoader(MySQLListener):

    def __init__(self):
        self.sql = {}
        self.numTables = 0
        self.numSelect = 0
        self.numWhere = 0
        self.numAlias = 0
        self.tableList = list()
        self.alias = dict()
        self.where = list()

    def getSQL(self):
        return self.sql

    def getSelectList(self,ctx):
        for i in range(ctx.getChildCount()):
            # print (i)
            child = ctx.getChild(i)
            if type(ctx.getChild(i)).__name__ == 'Select_listContext':
                return child.getText()

    def getTableRef(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'Table_referencesContext':
                return child.getText()

    def getWhere(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'Where_clauseContext':
                return child.getText()

    def commaCount(self,parse_string):
        return parse_string.count(',')

    def aliasCount(self,parse_string):
        return parse_string.count('.')

    def processSelect (self, parse_string):
        self.numSelect = (self.commaCount(parse_string) + 1)
        self.numAlias = self.aliasCount(parse_string)

        if self.numAlias > 0:
            temp_alias = parse_string.split('.')


    def processFrom(self, parse_string):
        self.numTables = (self.commaCount(parse_string) + 1)
        temp = parse_string.split(',')
        for x in range(self.numTables):
            key = 'table{}'.format(x)
            self.sql[key] = temp[x]


    # Enter a parse tree produced by MySQLParser#select_expression.
    def enterSelect_expression(self, ctx:MySQLParser.Select_expressionContext):
        selectList = self.getSelectList(ctx)
        table_ref = self.getTableRef(ctx)
        wher = self.getWhere(ctx)

        self.processFrom(table_ref)
        self.sql['SELECT'] = selectList
        self.sql['FROM'] = table_ref
        self.sql['WHERE'] = wher
