# Antlr4 Library
from antlr4 import *
from antlr4.InputStream import InputStream

# Library for parsing cluster.cfg
from lib.ClusterConfigGrammar.ClusterConfigLexer import ClusterConfigLexer
from lib.ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
from lib.ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener
from lib.ClusterConfigLoader import ClusterConfigLoader


def processCfg(clustercfg):
    cluster_input = FileStream(clustername)
    cluster_lexer = ClusterConfigLexer(cluster_input)
    cluster_stream = CommonTokenStream(cluster_lexer)
    cluster_parser = ClusterConfigParser(cluster_stream)
    cluster_tree = cluster_parser.config()

    cluster_loader = ClusterConfigLoader()
    cluster_walker = ParseTreeWalker()
    cluster_walker.walk(cluster_loader, cluster_tree)
    clustercfg = cluster_loader.getCFG()


if __name__ =="__main__":
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'clustercfg'
    if len(sys.argv) > 2:
        csvname = sys.argv[2]
    else:
        csvname = 'csvfile'

    (cataloginfo, nodeinfo, tablename, partitioninfo, numnodes) = processCfg(clustercfg)
    # PROCESSING CLUSTERCFG
    # [cataloginfo]
    # Mandatory
    # Dictionary with the keys: driver, hostname, username, passwd
    # can be used with catdb.getCatalogParams(cataloginfo) to get catalog connection parameters
    #
    # [nodeinfo]
    # Mandatory for running ddl (must be paired with a create table or drop table sql statement)
    # list of nodes containing dictionary with keys: nodeid, driver, hostname, username, passwd
    #
    # [tablename]
    # Mandatory for loading CSV files (must be paired with a csv file)
    # If a tablename is given then it is assumed that a csv file is being loaded.
    # String containing table name to be loaded in to.
    #
    # [partitioninfo]
    # Mandatory for loading CSV files (must be paired with a csv file)
    # Dictionary containing keys: method, column (not required when method=notpartition), partparam1 (if method=hash)
    #
    # [numnodes]
    # Optional
