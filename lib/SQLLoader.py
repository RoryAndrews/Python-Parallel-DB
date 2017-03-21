import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQL.MySQLParser import MySQLParser
from lib.MySQL.MySQLListener import MySQLListener

class SQLLoader(MySQLListener):

    def __init__(self):
        self.sql = {}
        self.alias = dict()
        self.expression = list()
        self.select = list()
        self.test = None

    def getSQL(self):
        return self.sql

    def getWhere(self,ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if type(child).__name__ == 'Where_clauseContext':
                return child.getText()

    def getExpression(self, ctx):
        # first child will have 2 or more children
        # 1st child is WHERE, 2nd child is expression, every other child in addition is an expression
        # The next generation is the bool primary, this one should have three children, predicate, relational_op, and preidcate
        
        return ctx.getChild(1).getChild(0).getChild(2).getText()

        # for i in range(1,ctx.getChildCount(),2):
        #
        # return ctx.getChild(1).getChild(0).getChildCount()

    def getSelect(self,ctx):
        self.select.insert(-1, (ctx.getChild(0).getChild(0).getText(), ctx.getChild(0).getChild(2).getText()))

    def getTables(self,ctx):
        for i in range(0,ctx.getChildCount(),2):
            self.alias['{}'.format(ctx.getChild(i).getChild(0).getChild(0).getChild(1).getText())] = ctx.getChild(i).getChild(0).getChild(0).getChild(0).getText()

    def enterDisplayed_column(self, ctx:MySQLParser.Displayed_columnContext):
        self.getSelect(ctx)

    def enterTable_references(self, ctx:MySQLParser.Table_referencesContext):
        self.getTables(ctx)

    def enterWhere_clause(self, ctx:MySQLParser.Where_clauseContext):
        self.test = self.getExpression(ctx)
