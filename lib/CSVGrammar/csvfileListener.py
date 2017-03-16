# Generated from csvfile.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .csvfileParser import csvfileParser
else:
    from csvfileParser import csvfileParser

# This class defines a complete listener for a parse tree produced by csvfileParser.
class csvfileListener(ParseTreeListener):

    # Enter a parse tree produced by csvfileParser#column.
    def enterColumn(self, ctx:csvfileParser.ColumnContext):
        pass

    # Exit a parse tree produced by csvfileParser#column.
    def exitColumn(self, ctx:csvfileParser.ColumnContext):
        pass


    # Enter a parse tree produced by csvfileParser#row.
    def enterRow(self, ctx:csvfileParser.RowContext):
        pass

    # Exit a parse tree produced by csvfileParser#row.
    def exitRow(self, ctx:csvfileParser.RowContext):
        pass


    # Enter a parse tree produced by csvfileParser#rows.
    def enterRows(self, ctx:csvfileParser.RowsContext):
        pass

    # Exit a parse tree produced by csvfileParser#rows.
    def exitRows(self, ctx:csvfileParser.RowsContext):
        pass


