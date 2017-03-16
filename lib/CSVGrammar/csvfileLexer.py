# Generated from csvfile.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\7")
        buf.write("\'\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\3\6\3\21\n\3\r\3\16\3\22\3\4\3\4\7\4\27\n\4\f\4\16")
        buf.write("\4\32\13\4\3\4\3\4\3\5\3\5\3\6\7\6!\n\6\f\6\16\6$\13\6")
        buf.write("\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\4\6\2\f\f\17\17")
        buf.write("$$..\5\2\f\f\17\17$$)\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\20\3\2\2\2")
        buf.write("\7\24\3\2\2\2\t\35\3\2\2\2\13\"\3\2\2\2\r\16\7.\2\2\16")
        buf.write("\4\3\2\2\2\17\21\n\2\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22")
        buf.write("\20\3\2\2\2\22\23\3\2\2\2\23\6\3\2\2\2\24\30\5\t\5\2\25")
        buf.write("\27\n\3\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2")
        buf.write("\30\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\5\t\5")
        buf.write("\2\34\b\3\2\2\2\35\36\7$\2\2\36\n\3\2\2\2\37!\7\17\2\2")
        buf.write(" \37\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2")
        buf.write("$\"\3\2\2\2%&\7\f\2\2&\f\3\2\2\2\6\2\22\30\"\2")
        return buf.getvalue()


class csvfileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    COMMA = 1
    STUFF = 2
    STRING = 3
    QUOTE = 4
    NEWLINE = 5

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "STUFF", "STRING", "QUOTE", "NEWLINE" ]

    ruleNames = [ "COMMA", "STUFF", "STRING", "QUOTE", "NEWLINE" ]

    grammarFileName = "csvfile.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


