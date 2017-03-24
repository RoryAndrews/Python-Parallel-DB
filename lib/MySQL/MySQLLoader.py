import sys

from antlr4 import *
from antlr4.InputStream import InputStream

if __name__ is not None and "." in __name__:
    from .MySQLParser import MySQLParser
    from .MySQLListener import MySQLListener
else:
    from MySQLParser import MySQLParser
    from MySQLListener import MySQLListener

class MySQLLoader(MySQLListener):
    def __init__(self):
        self.columns = list()
        self.comparisons = list()
        self.aliases = dict()
        self.sqltype = None

    # Exit a parse tree produced by MySQLParser#bool_primary.
    def exitBool_primary(self, ctx:MySQLParser.Bool_primaryContext):
        if ctx.getChildCount() == 3:
            self.comparisons.append((ctx.getChild(0).getText(), ctx.getChild(2).getText()))

    # Exit a parse tree produced by MySQLParser#column_spec.
    def exitColumn_spec(self, ctx:MySQLParser.Column_specContext):
        table = None
        column = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, MySQLParser.Table_nameContext):
                table = child.getText()
            if isinstance(child, MySQLParser.Column_nameContext):
                column = child.getText()

        if table and column:
            self.columns.append((table, column))

    # Exit a parse tree produced by MySQLParser#table_factor.
    def exitTable_factor(self, ctx:MySQLParser.Table_factorContext):
        tablename = None
        alias = None
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, MySQLParser.Table_specContext):
                tablename = child.getText()
            if isinstance(child, MySQLParser.AliasContext):
                alias = child.getText()

        if tablename:
            self.aliases[alias] = tablename

    def enterData_manipulation_statements(self, ctx:MySQLParser.Data_manipulation_statementsContext):
        # print(type(ctx.getChild(0)).__name__)
        child = ctx.getChild(0)

        if isinstance(child, MySQLParser.Select_statementContext):
            self.sqltype = "select"
        elif isinstance(child, MySQLParser.Insert_statementsContext):
            self.sqltype = "insert"
        elif isinstance(child, MySQLParser.Delete_statementsContext):
            self.sqltype = "delete"
        else:
            self.sqltype = "update"
