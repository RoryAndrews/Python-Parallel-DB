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
        sqlfile.close()
    except:
        print("runSQL: Could not read file.")
        return False
    # Check if create table or drop table and use runDDL if true.
    try:
        if re.search("CREATE TABLE", sqlstatement, flags=re.IGNORECASE | re.MULTILINE) or re.search("DROP TABLE", sqlstatement, flags=re.IGNORECASE | re.MULTILINE):
            return runDDL(cataloginfo, numnodes, nodeinfo, sqlfilename)

    except BaseException as e:
        print(str(e))
        print("Error in runSQL: Could not parse sql statement.")

    (sqltype, aliases, columns, comparisons) = processSQL(sqlfilename)
    if sqltype == 'select':
        pass
    else:
        print("runSQL: Only CREATE TABLE, DROP TABLE, and SELECT statements are allowed.")




if __name__ =="__main__":
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        print("Not enough arguements given.")
        quit()
    if len(sys.argv) > 2:
        filename = sys.argv[2]
        filetype = filename.split(".")
    else:
        print("Not enough arguements given.")
        quit()

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)
    try:
        if filetype[1] == "ddl":
            (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)
            runDDL(cataloginfo, numnodes, nodeinfo, filename)
            quit()
    except:
        pass
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
