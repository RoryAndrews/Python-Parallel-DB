import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQL.MySQLParser import MySQLParser
from lib.MySQL.MySQLListener import MySQLListener

class SQLLoader(MySQLListener):

    def __init__(self):
        self.sql = {}

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

    # Enter a parse tree produced by MySQLParser#select_expression.
    def enterSelect_expression(self, ctx:MySQLParser.Select_expressionContext):
        selectList = self.getSelectList(ctx)
        table_ref = self.getTableRef(ctx)
        # wher = self.getWhere(ctx)
        wher = self.getWhere(ctx)
        self.sql['SELECT'] = selectList
        self.sql['FROM'] = table_ref
        self.sql['WHERE'] = wher
