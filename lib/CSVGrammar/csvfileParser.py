# Generated from csvfile.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\7")
        buf.write("\35\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\5\2\f\n\2\3\3")
        buf.write("\3\3\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\3\3\3\3\4\6\4\31")
        buf.write("\n\4\r\4\16\4\32\3\4\2\2\5\2\4\6\2\2\35\2\13\3\2\2\2\4")
        buf.write("\r\3\2\2\2\6\30\3\2\2\2\b\f\7\5\2\2\t\f\7\4\2\2\n\f\3")
        buf.write("\2\2\2\13\b\3\2\2\2\13\t\3\2\2\2\13\n\3\2\2\2\f\3\3\2")
        buf.write("\2\2\r\22\5\2\2\2\16\17\7\3\2\2\17\21\5\2\2\2\20\16\3")
        buf.write("\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\25")
        buf.write("\3\2\2\2\24\22\3\2\2\2\25\26\7\7\2\2\26\5\3\2\2\2\27\31")
        buf.write("\5\4\3\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\7\3\2\2\2\5\13\22\32")
        return buf.getvalue()


class csvfileParser ( Parser ):

    grammarFileName = "csvfile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "<INVALID>", "<INVALID>", "'\"'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "STUFF", "STRING", "QUOTE", 
                      "NEWLINE" ]

    RULE_column = 0
    RULE_row = 1
    RULE_rows = 2

    ruleNames =  [ "column", "row", "rows" ]

    EOF = Token.EOF
    COMMA=1
    STUFF=2
    STRING=3
    QUOTE=4
    NEWLINE=5

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ColumnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(csvfileParser.STRING, 0)

        def STUFF(self):
            return self.getToken(csvfileParser.STUFF, 0)

        def getRuleIndex(self):
            return csvfileParser.RULE_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn" ):
                listener.enterColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn" ):
                listener.exitColumn(self)




    def column(self):

        localctx = csvfileParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_column)
        try:
            self.state = 9
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [csvfileParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(csvfileParser.STRING)
                pass
            elif token in [csvfileParser.STUFF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.match(csvfileParser.STUFF)
                pass
            elif token in [csvfileParser.COMMA, csvfileParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csvfileParser.ColumnContext)
            else:
                return self.getTypedRuleContext(csvfileParser.ColumnContext,i)


        def NEWLINE(self):
            return self.getToken(csvfileParser.NEWLINE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(csvfileParser.COMMA)
            else:
                return self.getToken(csvfileParser.COMMA, i)

        def getRuleIndex(self):
            return csvfileParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = csvfileParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.column()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==csvfileParser.COMMA:
                self.state = 12
                self.match(csvfileParser.COMMA)
                self.state = 13
                self.column()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self.match(csvfileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(csvfileParser.RowContext)
            else:
                return self.getTypedRuleContext(csvfileParser.RowContext,i)


        def getRuleIndex(self):
            return csvfileParser.RULE_rows

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRows" ):
                listener.enterRows(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRows" ):
                listener.exitRows(self)




    def rows(self):

        localctx = csvfileParser.RowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.row()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << csvfileParser.COMMA) | (1 << csvfileParser.STUFF) | (1 << csvfileParser.STRING) | (1 << csvfileParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





