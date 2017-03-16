# Generated from ClusterConfig.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\22")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\'")
        buf.write("\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\6\tN\n\t")
        buf.write("\r\t\16\tO\3\n\3\n\3\n\3\n\3\13\6\13W\n\13\r\13\16\13")
        buf.write("X\3\f\6\f\\\n\f\r\f\16\f]\3\r\6\ra\n\r\r\r\16\rb\3\r\2")
        buf.write("\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4\3\2\20\21\4\2")
        buf.write("\t\n\f\21c\2\33\3\2\2\2\4&\3\2\2\2\6(\3\2\2\2\b.\3\2\2")
        buf.write("\2\n\64\3\2\2\2\f;\3\2\2\2\16D\3\2\2\2\20J\3\2\2\2\22")
        buf.write("Q\3\2\2\2\24V\3\2\2\2\26[\3\2\2\2\30`\3\2\2\2\32\34\5")
        buf.write("\4\3\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36")
        buf.write("\3\2\2\2\36\3\3\2\2\2\37\'\5\6\4\2 \'\5\b\5\2!\'\5\n\6")
        buf.write("\2\"\'\5\f\7\2#\'\5\16\b\2$\'\5\20\t\2%\'\5\22\n\2&\37")
        buf.write("\3\2\2\2& \3\2\2\2&!\3\2\2\2&\"\3\2\2\2&#\3\2\2\2&$\3")
        buf.write("\2\2\2&%\3\2\2\2\'\5\3\2\2\2()\7\3\2\2)*\7\f\2\2*+\5\26")
        buf.write("\f\2+,\7\13\2\2,-\5\30\r\2-\7\3\2\2\2./\7\4\2\2/\60\7")
        buf.write("\f\2\2\60\61\5\26\f\2\61\62\7\13\2\2\62\63\5\30\r\2\63")
        buf.write("\t\3\2\2\2\64\65\7\5\2\2\65\66\5\24\13\2\66\67\7\f\2\2")
        buf.write("\678\5\26\f\289\7\13\2\29:\5\30\r\2:\13\3\2\2\2;<\7\6")
        buf.write("\2\2<=\7\f\2\2=>\7\5\2\2>?\5\24\13\2?@\7\f\2\2@A\5\26")
        buf.write("\f\2AB\7\13\2\2BC\5\30\r\2C\r\3\2\2\2DE\7\6\2\2EF\7\f")
        buf.write("\2\2FG\5\26\f\2GH\7\13\2\2HI\5\30\r\2I\17\3\2\2\2JK\7")
        buf.write("\7\2\2KM\7\13\2\2LN\7\20\2\2ML\3\2\2\2NO\3\2\2\2OM\3\2")
        buf.write("\2\2OP\3\2\2\2P\21\3\2\2\2QR\7\b\2\2RS\7\13\2\2ST\5\26")
        buf.write("\f\2T\23\3\2\2\2UW\7\20\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2")
        buf.write("\2\2XY\3\2\2\2Y\25\3\2\2\2Z\\\t\2\2\2[Z\3\2\2\2\\]\3\2")
        buf.write("\2\2][\3\2\2\2]^\3\2\2\2^\27\3\2\2\2_a\t\3\2\2`_\3\2\2")
        buf.write("\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\31\3\2\2\2\b\35&OX]")
        buf.write("b")
        return buf.getvalue()


class ClusterConfigParser ( Parser ):

    grammarFileName = "ClusterConfig.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'catalog'", "'localnode'", "'node'", 
                     "'partition'", "'numnodes'", "'tablename'", "':'", 
                     "'/'", "'='", "'.'", "'_'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "COLON", "SLASH", 
                      "EQUALS", "DOT", "UNDERSCORE", "PLUS", "MINUS", "NUM", 
                      "CHARS", "WS" ]

    RULE_config = 0
    RULE_stat = 1
    RULE_catalog_info = 2
    RULE_localnode_info = 3
    RULE_node_info = 4
    RULE_partition_node_info = 5
    RULE_partition_info = 6
    RULE_numnodes = 7
    RULE_tablename = 8
    RULE_nodeid = 9
    RULE_key = 10
    RULE_value = 11

    ruleNames =  [ "config", "stat", "catalog_info", "localnode_info", "node_info", 
                   "partition_node_info", "partition_info", "numnodes", 
                   "tablename", "nodeid", "key", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    COLON=7
    SLASH=8
    EQUALS=9
    DOT=10
    UNDERSCORE=11
    PLUS=12
    MINUS=13
    NUM=14
    CHARS=15
    WS=16

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ConfigContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ClusterConfigParser.StatContext)
            else:
                return self.getTypedRuleContext(ClusterConfigParser.StatContext,i)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfig" ):
                listener.enterConfig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfig" ):
                listener.exitConfig(self)




    def config(self):

        localctx = ClusterConfigParser.ConfigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.stat()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.T__0) | (1 << ClusterConfigParser.T__1) | (1 << ClusterConfigParser.T__2) | (1 << ClusterConfigParser.T__3) | (1 << ClusterConfigParser.T__4) | (1 << ClusterConfigParser.T__5))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catalog_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Catalog_infoContext,0)


        def localnode_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Localnode_infoContext,0)


        def node_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Node_infoContext,0)


        def partition_node_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Partition_node_infoContext,0)


        def partition_info(self):
            return self.getTypedRuleContext(ClusterConfigParser.Partition_infoContext,0)


        def numnodes(self):
            return self.getTypedRuleContext(ClusterConfigParser.NumnodesContext,0)


        def tablename(self):
            return self.getTypedRuleContext(ClusterConfigParser.TablenameContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = ClusterConfigParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.catalog_info()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.localnode_info()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.node_info()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.partition_node_info()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.partition_info()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.numnodes()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 35
                self.tablename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catalog_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_catalog_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatalog_info" ):
                listener.enterCatalog_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatalog_info" ):
                listener.exitCatalog_info(self)




    def catalog_info(self):

        localctx = ClusterConfigParser.Catalog_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_catalog_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ClusterConfigParser.T__0)
            self.state = 39
            self.match(ClusterConfigParser.DOT)
            self.state = 40
            self.key()
            self.state = 41
            self.match(ClusterConfigParser.EQUALS)
            self.state = 42
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Localnode_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_localnode_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalnode_info" ):
                listener.enterLocalnode_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalnode_info" ):
                listener.exitLocalnode_info(self)




    def localnode_info(self):

        localctx = ClusterConfigParser.Localnode_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_localnode_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ClusterConfigParser.T__1)
            self.state = 45
            self.match(ClusterConfigParser.DOT)
            self.state = 46
            self.key()
            self.state = 47
            self.match(ClusterConfigParser.EQUALS)
            self.state = 48
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeid(self):
            return self.getTypedRuleContext(ClusterConfigParser.NodeidContext,0)


        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_node_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_info" ):
                listener.enterNode_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_info" ):
                listener.exitNode_info(self)




    def node_info(self):

        localctx = ClusterConfigParser.Node_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_node_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ClusterConfigParser.T__2)
            self.state = 51
            self.nodeid()
            self.state = 52
            self.match(ClusterConfigParser.DOT)
            self.state = 53
            self.key()
            self.state = 54
            self.match(ClusterConfigParser.EQUALS)
            self.state = 55
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Partition_node_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.DOT)
            else:
                return self.getToken(ClusterConfigParser.DOT, i)

        def nodeid(self):
            return self.getTypedRuleContext(ClusterConfigParser.NodeidContext,0)


        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_partition_node_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartition_node_info" ):
                listener.enterPartition_node_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartition_node_info" ):
                listener.exitPartition_node_info(self)




    def partition_node_info(self):

        localctx = ClusterConfigParser.Partition_node_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_partition_node_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ClusterConfigParser.T__3)
            self.state = 58
            self.match(ClusterConfigParser.DOT)
            self.state = 59
            self.match(ClusterConfigParser.T__2)
            self.state = 60
            self.nodeid()
            self.state = 61
            self.match(ClusterConfigParser.DOT)
            self.state = 62
            self.key()
            self.state = 63
            self.match(ClusterConfigParser.EQUALS)
            self.state = 64
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Partition_infoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(ClusterConfigParser.DOT, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def value(self):
            return self.getTypedRuleContext(ClusterConfigParser.ValueContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_partition_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPartition_info" ):
                listener.enterPartition_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPartition_info" ):
                listener.exitPartition_info(self)




    def partition_info(self):

        localctx = ClusterConfigParser.Partition_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_partition_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ClusterConfigParser.T__3)
            self.state = 67
            self.match(ClusterConfigParser.DOT)
            self.state = 68
            self.key()
            self.state = 69
            self.match(ClusterConfigParser.EQUALS)
            self.state = 70
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumnodesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_numnodes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumnodes" ):
                listener.enterNumnodes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumnodes" ):
                listener.exitNumnodes(self)




    def numnodes(self):

        localctx = ClusterConfigParser.NumnodesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_numnodes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ClusterConfigParser.T__4)
            self.state = 73
            self.match(ClusterConfigParser.EQUALS)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.match(ClusterConfigParser.NUM)
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TablenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ClusterConfigParser.EQUALS, 0)

        def key(self):
            return self.getTypedRuleContext(ClusterConfigParser.KeyContext,0)


        def getRuleIndex(self):
            return ClusterConfigParser.RULE_tablename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTablename" ):
                listener.enterTablename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTablename" ):
                listener.exitTablename(self)




    def tablename(self):

        localctx = ClusterConfigParser.TablenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tablename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ClusterConfigParser.T__5)
            self.state = 80
            self.match(ClusterConfigParser.EQUALS)
            self.state = 81
            self.key()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NodeidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_nodeid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeid" ):
                listener.enterNodeid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeid" ):
                listener.exitNodeid(self)




    def nodeid(self):

        localctx = ClusterConfigParser.NodeidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nodeid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.match(ClusterConfigParser.NUM)
                self.state = 86 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHARS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.CHARS)
            else:
                return self.getToken(ClusterConfigParser.CHARS, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ClusterConfigParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==ClusterConfigParser.NUM or _la==ClusterConfigParser.CHARS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ClusterConfigParser.NUM or _la==ClusterConfigParser.CHARS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.PLUS)
            else:
                return self.getToken(ClusterConfigParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.MINUS)
            else:
                return self.getToken(ClusterConfigParser.MINUS, i)

        def CHARS(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.CHARS)
            else:
                return self.getToken(ClusterConfigParser.CHARS, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.NUM)
            else:
                return self.getToken(ClusterConfigParser.NUM, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.DOT)
            else:
                return self.getToken(ClusterConfigParser.DOT, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.SLASH)
            else:
                return self.getToken(ClusterConfigParser.SLASH, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.COLON)
            else:
                return self.getToken(ClusterConfigParser.COLON, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(ClusterConfigParser.UNDERSCORE)
            else:
                return self.getToken(ClusterConfigParser.UNDERSCORE, i)

        def getRuleIndex(self):
            return ClusterConfigParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ClusterConfigParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.COLON) | (1 << ClusterConfigParser.SLASH) | (1 << ClusterConfigParser.DOT) | (1 << ClusterConfigParser.UNDERSCORE) | (1 << ClusterConfigParser.PLUS) | (1 << ClusterConfigParser.MINUS) | (1 << ClusterConfigParser.NUM) | (1 << ClusterConfigParser.CHARS))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClusterConfigParser.COLON) | (1 << ClusterConfigParser.SLASH) | (1 << ClusterConfigParser.DOT) | (1 << ClusterConfigParser.UNDERSCORE) | (1 << ClusterConfigParser.PLUS) | (1 << ClusterConfigParser.MINUS) | (1 << ClusterConfigParser.NUM) | (1 << ClusterConfigParser.CHARS))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





