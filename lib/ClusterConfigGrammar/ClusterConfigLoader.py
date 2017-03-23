import sys
from antlr4 import *
from antlr4.InputStream import InputStream

if __name__ is not None and "." in __name__:
    from .ClusterConfigParser import ClusterConfigParser
    from .ClusterConfigListener import ClusterConfigListener
else:
    from ClusterConfigParser import ClusterConfigParser
    from ClusterConfigListener import ClusterConfigListener

class ClusterConfigLoader(ClusterConfigListener):

    def __init__(self):
        self.cfg = {}

    def getCFG(self):
        return self.cfg

    def getKey(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ClusterConfigParser.KeyContext):
                return child.getText()

    def getValue(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ClusterConfigParser.ValueContext):
                return child.getText()

    def getNodeId(self, ctx):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, ClusterConfigParser.NodeidContext):
                return int(child.getText())

    # Exit a parse tree produced by ClusterConfigParser#catalog_info.
    def exitCatalog_info(self, ctx:ClusterConfigParser.Catalog_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)

        if 'catalog' not in self.cfg:
            self.cfg['catalog'] = dict()
        self.cfg['catalog'][key] = value

    # Exit a parse tree produced by ClusterConfigParser#partition_node_info.
    def exitPartition_node_info(self, ctx:ClusterConfigParser.Partition_node_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        nodeid = self.getNodeId(ctx)

        if 'partitionnodeinfo' not in self.cfg:
            self.cfg['partitionnodeinfo'] = list()
        try:
            index = next(i for i,node in enumerate(self.cfg['partitionnodeinfo']) if node['nodeid'] == nodeid)
            self.cfg['partitionnodeinfo'][index][key] = value
        except StopIteration:
            self.cfg['partitionnodeinfo'].append({'nodeid': nodeid, key:value})

    # Exit a parse tree produced by ClusterConfigParser#node_info.
    def exitNode_info(self, ctx:ClusterConfigParser.Node_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        nodeid = self.getNodeId(ctx)

        if 'nodeinfo' not in self.cfg:
            self.cfg['nodeinfo'] = list()
        try:
            index = next(i for i,node in enumerate(self.cfg['nodeinfo']) if node['nodeid'] == nodeid)
            self.cfg['nodeinfo'][index][key] = value
        except StopIteration:
            self.cfg['nodeinfo'].append({'nodeid': nodeid, key:value})

    # Exit a parse tree produced by ClusterConfigParser#partition_info.
    def exitPartition_info(self, ctx:ClusterConfigParser.Partition_infoContext):
        key = self.getKey(ctx)
        value = self.getValue(ctx)
        if 'partitioninfo' not in self.cfg:
            self.cfg['partitioninfo'] = dict()
        self.cfg['partitioninfo'][key] = value

    # Exit a parse tree produced by ClusterConfigParser#numnodes.
    def exitNumnodes(self, ctx:ClusterConfigParser.NumnodesContext):
        self.cfg['numnodes'] = int(ctx.getChild(2).getText())

    # Exit a parse tree produced by ClusterConfigParser#tablename.
    def exitTablename(self, ctx:ClusterConfigParser.TablenameContext):
        self.cfg['tablename'] = ctx.getChild(2).getText()
