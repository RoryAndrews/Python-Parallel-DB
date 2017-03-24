import sys

from processSQL import *
from lib import cfgProcessor
from loadCSV import *
from runDDL import *


def runSQL(cataloginfo, numnodes, nodeinfo, sqlfilename):
    # First try to read file.
    try:
        sqlfile = open(sqlfilename)
        sqlstatement = sqlfile.read()
    except:
        print("runSQL: Could not read file.")
        return False
    # Check if create table or drop table and use runDDL if true.
    try:
        if re.search("CREATE TABLE", sqlstatement, flags=re.IGNORECASE | re.MULTILINE) or re.search("DROP TABLE", sqlstatement, flags=re.IGNORECASE | re.MULTILINE):
            return runDDL(cataloginfo, numnodes, nodeinfo, sqlfilename)
        else:
            (sqltype, alias, column_list) = processSQL(sqlfilename)
    except:
        print("Error in runSQL: Could not parse sql statement.")
        return False

    if sqltype == 'select':
        print("Inside select.")
    else:
        print("runSQL: Only CREATE TABLE, DROP TABLE, and SELECT statements are allowed.")




if __name__ =="__main__":
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'cluster.cfg'
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = None

    # (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.processCfg(clustername)
    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)

    # PROCESSING CLUSTERCFG
    # [cataloginfo]
    # Mandatory
    # Dictionary with the keys: driver, hostname, username, passwd
    # can be used with catdb.getCatalogParams(cataloginfo) to get catalog connection parameters
    #
    # [numnodes]
    # Optional
    #
    # [nodeinfo]
    # Mandatory for running ddl (must be paired with a create table or drop table sql statement)
    # list of nodes containing dictionaries with keys: nodeid, driver, hostname, username, passwd
    #
    # [tablename]
    # Mandatory for loading CSV files (must be paired with a csv file)
    # If a tablename is given then it is assumed that a csv file is being loaded.
    # String containing table name to be loaded in to.
    #
    # [partitioninfo]
    # Mandatory for loading CSV files (must be paired with a csv file)
    # Dictionary containing keys: method, column (not required when method=notpartition), param1 (if method=hash)
    #
    # [partitionnodeinfo]
    # Mandatory for range partitioning (must be paired with a csv file)
    # list of nodes containing dictionaries with keys: param1, param2

    if cataloginfo:
        if tablename:
            loadCSV(
                cataloginfo=cataloginfo, numnodes=numnodes, tablename=tablename,
                partitioninfo=partitioninfo, partitionnodeinfo=partitionnodeinfo,
                csvfilename=filename
            )
        else:
            runSQL(cataloginfo=cataloginfo, numnodes=numnodes, nodeinfo=nodeinfo, sqlfilename=filename)
    else:
        print("ERROR: Cluster configuration file could not be used.")
