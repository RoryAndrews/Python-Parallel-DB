import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from lib.MySQL.MySQLParser import MySQLParser
from lib.MySQL.MySQLListener import MySQLListener

class SQLLoader(MySQLListener):

    def __init__(self):
        self.sql = {}
        self.alias = dict()
        self.where = list()
        self.select = list()
        self.test = None

    def getSQL(self):
        return self.sql

    def getWhere(self, ctx):
        temp_table1 = None
        temp_table2 = None
        temp_col1 = None
        temp_col2 = None
        temp_relation = None
        expression = list()

        if ctx.getChildCount() == 0:
            return None
        # if the context has a where clause it will have at least two children
        #1ST GEN: 1st child is WHERE, 2nd child is expression, every other child in addition is an expression
        #2ND GEN: The next generation is the bool primary, this one should have three children, predicate, relational_op, and preidcate
        # If the predicate is simple, then you can stop at this level, if it is not continue
        #8TH GEN: For a complex predicate you must go down to the 8th gen to get the escape clause
        else:
            for i in range(1,ctx.getChildCount(),2):
                gen1 = self.visitChild(ctx,i)
                for j in range (0, gen1.getChild(0).getChildCount(),2):
                    gen2 = gen1.getChild(0)
                    # print (type(gen2).__name__)
                    if temp_relation == None:
                        temp_relation = self.visitChild(gen2,j+1).getText()
                    if temp_col1 == None:
                        temp_col1 = self.visitChild(gen2,j).getText()
                    else:
                        temp_col2 = self.visitChild(gen2,j).getText()

                    if temp_col1 != None and temp_col2 != None:
                        expression.insert(-1, (temp_col1, temp_relation, temp_col2))
                        temp_col1 = None
                        temp_col2 = None
                        temp_relation = None

        # getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0)
        # for i in range(1,ctx.getChildCount(),2):
        #
        # return ctx.getChild(1).getChild(0).getChildCount()
        return expression

    def visitChild(self, ctx, branch):
        return ctx.getChild(branch)

    def getSelect(self,ctx):
        # print(ctx.getText())
        for i in range(0,ctx.getChildCount(),2):
            gen1 = self.visitChild(ctx,i)
            self.select.insert(-1, (gen1.getChild(0).getText(), gen1.getChild(2).getText()))

    def getFrom(self,ctx):
        for i in range(0,ctx.getChildCount(),2):
            gen1 = self.visitChild(ctx, i)
            if gen1.getChild(0).getChild(0).getChildCount() > 1:
                self.alias['{}'.format(gen1.getChild(0).getChild(0).getChild(1).getText())] = gen1.getChild(0).getChild(0).getChild(0).getText()
            else:
                self.alias['{}'.format(None)] = gen1.getChild(0).getChild(0).getChild(0).getText()

    def enterDisplayed_column(self, ctx:MySQLParser.Displayed_columnContext):
        # print(type(ctx.getChild(0)).__name__)
        self.getSelect(ctx)

    def enterTable_references(self, ctx:MySQLParser.Table_referencesContext):
        self.getFrom(ctx)

    def enterWhere_clause(self, ctx:MySQLParser.Where_clauseContext):
        self.where = self.getWhere(ctx)
