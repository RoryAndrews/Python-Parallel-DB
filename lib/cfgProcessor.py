import sys

# Antlr4 Library
from antlr4 import *

# Library for parsing cluster.cfg
if __name__ == "__main__":
    from ClusterConfigGrammar.ClusterConfigLexer import ClusterConfigLexer
    from ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
    from ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener
    from ClusterConfigGrammar.ClusterConfigLoader import ClusterConfigLoader
else:
    from lib.ClusterConfigGrammar.ClusterConfigLexer import ClusterConfigLexer
    from lib.ClusterConfigGrammar.ClusterConfigParser import ClusterConfigParser
    from lib.ClusterConfigGrammar.ClusterConfigListener import ClusterConfigListener
    from lib.ClusterConfigGrammar.ClusterConfigLoader import ClusterConfigLoader

def process(clustername):
    clustercfg = getClusterCfg(clustername)
    if clustercfg:
        return processCfg(clustercfg)


def getClusterCfg(clustername):
    try:
        cluster_input = FileStream(clustername)
        cluster_lexer = ClusterConfigLexer(cluster_input)
        cluster_stream = CommonTokenStream(cluster_lexer)
        cluster_parser = ClusterConfigParser(cluster_stream)
        cluster_tree = cluster_parser.config()

        cluster_loader = ClusterConfigLoader()
        cluster_walker = ParseTreeWalker()
        cluster_walker.walk(cluster_loader, cluster_tree)
        clustercfg = cluster_loader.getCFG()
    except BaseException as e:
        print(str(e))
        print("cfgProcessor: Failed to parse cluster config file.")
        clustercfg = None

    return clustercfg

# Returns cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo
def processCfg(clustercfg):
    # [cataloginfo]
    # Dictionary with the keys: driver, hostname, username, passwd
    cataloginfo = None
    if 'catalog' in clustercfg:
        keys_needed = set(['driver', 'hostname', 'username', 'passwd'])
        keys = set(clustercfg['catalog'].keys())
        if not keys_needed.issubset(keys): # if keys_needed is not in keys then not enough keys were provided.
            print("Cluster Config Error: catalog_info (defined by lines like: catalog.key=value) does not contain all the necessary keys.")
            print("Missing key(s): {}".format(keys_needed - keys))
        else:
            cataloginfo = clustercfg['catalog']
    else:
        print("Cluster Config Error: Failed to locate catalog connection info.")

    # [nodeinfo]
    # list of nodes containing dictionary with keys: nodeid, driver, hostname, username, passwd
    nodeinfo = None
    if 'nodeinfo' in clustercfg:
        keys_needed = set(['nodeid', 'driver', 'hostname', 'username', 'passwd'])
        for node in clustercfg['nodeinfo']:
            keys = set(node.keys())
            if not keys_needed.issubset(keys): # if keys_needed is not in keys then not enough keys were provided.
                print("Cluster Config Error: A node_info node [nodeid:{}] (defined by lines like: node#.key=value) does not contain all the necessary keys.".format(node['nodeid']))
                print("Missing key(s): {}".format(keys_needed - keys))
                nodeinfo = None
                break
            else:
                nodeinfo = True
        if nodeinfo: # True if all nodeinfo was valid, otherwise None (false)
            nodeinfo = clustercfg['nodeinfo']

    # [tablename]
    # String containing table name to be loaded in to.
    tablename = None
    if 'tablename' in clustercfg:
        tablename = clustercfg['tablename']

    # [partitioninfo]
    # Mandatory for loading CSV files (must be paired with a csv file)
    # Dictionary containing keys: method, column (not required when method=notpartition), param1 (if method=hash)
    partitioninfo = None
    if 'partitioninfo' in clustercfg:
        keys_needed = set(['method'])
        keys = set(clustercfg['partitioninfo'].keys())
        if not keys_needed.issubset(keys): # if keys_needed is not in keys then not enough keys were provided.
            print("Cluster Config Error: partition_info (defined by lines like: partition.key=value) does not contain all the necessary keys.")
            print("Missing key(s): {}".format(keys_needed - keys))
        else:
            partitioninfo = clustercfg['partitioninfo']
            # If method = range or hash then you need a key called column
            if (partitioninfo['method'] == 'range' or partitioninfo['method'] == 'hash') and not 'column' in partitioninfo:
                print("Cluster Config Error: partition_info is missing key named column (required when method=range or method=hash)")
                partitioninfo = None
            # Need param1 if method=hash
            elif partitioninfo['method'] == 'hash' and not ('param1' in partitioninfo):
                print("Cluster Config Error: partition_info is missing key named param1 (required when method=hash)")
                partitioninfo = None

    # [partitionnodeinfo]
    # list of nodes containing dictionaries with keys: param1, param2
    partitionnodeinfo = None
    if 'partitionnodeinfo' in clustercfg:
        keys_needed = set(['param1', 'param2', 'nodeid'])
        for node in clustercfg['partitionnodeinfo']:
            keys = set(node.keys())
            if not keys_needed.issubset(keys): # if keys_needed is not in keys then not enough keys were provided.
                print("Cluster Config Error: partition_node_info [nodeid:{}] (defined by lines like: partition.node#.key=value) does not contain all the necessary keys.".format(node['nodeid']))
                print("Missing key(s): {}".format(keys_needed - keys))
                partitionnodeinfo = None
            else:
                partitionnodeinfo = True
        if partitionnodeinfo:
            partitionnodeinfo = clustercfg['partitionnodeinfo']

    # [numnodes]
    # Optional
    numnodes = None
    if 'numnodes' in clustercfg:
        numnodes = clustercfg['numnodes']
        if tablename and partitionnodeinfo:
            if not (len(partitionnodeinfo) == numnodes):
                print("Cluster Config Error: numnodes is not equal to the number of nodes given in the config for partitioning.")
                print("Setting numnodes to be equal to number of nodes in the config: From {} to {}".format(numnodes, len(partitionnodeinfo)))
        elif nodeinfo:
            if not len(nodeinfo) == numnodes:
                print("Cluster Config Error: numnodes is not equal to the number of nodes given in the config for connecting.")
                print("Setting numnodes to be equal to number of nodes in the config: From {} to {}".format(numnodes, len(nodeinfo)))
    else:
        if tablename and partitionnodeinfo:
            numnodes = len(partitionnodeinfo)
        elif nodeinfo:
            numnodes = len(nodeinfo)

    if nodeinfo:
        sorted(nodeinfo, key=lambda x: x['nodeid'])
        for index, node in enumerate(nodeinfo):
            if not (index + 1 == node['nodeid']):
                nodeinfo = None
                print("Cluster Config Error: nodeinfo (defined by lines like node#.key=value) nodeids were not complete (must start at 1 and there can not be a gap i.e. 1,2,4,5).")
                print("Problem node id: {} (was expecting nodeid={})".format(node, index+1))
                break

    if partitionnodeinfo:
        sorted(partitionnodeinfo, key=lambda x: x['nodeid'])
        for index, node in enumerate(partitionnodeinfo):
            if not (index + 1 == node['nodeid']):
                partitionnodeinfo = None
                print("Cluster Config Error: partitionnodeinfo (defined by lines like partition.node#.key=value) nodeids were not complete (must start at 1 and there can not be a gap i.e. 1,2,4,5).")
                print("Problem node id: {} (was expecting nodeid={})".format(node, index+1))
                break



    return (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'clustertestparse.cfg'

    print("clustername: {}".format(clustername))

    clustercfg = getClusterCfg(clustername)

    print("Clustercfg:")
    print(clustercfg)

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = process(clustername)

    print("\ncataloginfo:\n{}".format(cataloginfo))
    print("\nnumnodes:\n{}".format(numnodes))
    print("\nnodeinfo:\n{}".format(nodeinfo))
    print("\ntablename:\n{}".format(tablename))
    print("\npartitioninfo:\n{}".format(partitioninfo))
    print("\npartitionnodeinfo:\n{}".format(partitionnodeinfo))
