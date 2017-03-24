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
        filetype = filename.split(".")
    else:
        filename = None

    # (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.processCfg(clustername)
    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)

    if filetype[1] == "ddl":
        (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)
        cparams = catdb.getCatalogParams(cataloginfo)
        runDDL(cataloginfo, numnodes, nodeinfo, filename)

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
