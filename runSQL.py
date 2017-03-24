import sys
import re

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
    print("sqltype: {}, aliases: {}, columns: {}, comparisons: {}".format(sqltype, aliases, columns, comparisons))
    if sqltype == 'select':
        if checkForJoin(comparisons):
            return joinQuery(cataloginfo, aliases, columns, sqlstatement, sqlfilename)
        else:
            print("Normal query.")
    else:
        print("runSQL: Only CREATE TABLE, DROP TABLE, and SELECT statements are allowed.")


def joinQuery(cataloginfo, aliases, columns, sqlstatement, sqlfilename):
    cparams = catdb.getCatalogParams(cataloginfo)

    if len(aliases) > 2:
        print("runSQL: More than two tables in a query is not allowed.")
        return False
    elif len(aliases) < 2:
        print("runSQL: Can't perform a join with one Table.")
        return False

    partitionedsql = getPartitionedQuery(sqlstatement, aliases, columns)

# Returns string where
def getPartitionedQuery(sqlstatement, aliases, columns):
    aliaslist = list()
    for key, value in aliases.items():
        if not value:
            aliaslist.append(key)
        else:
            aliaslist.append(value)

    for alias in aliaslist:
        sqlstatement = re.sub("([\s(])({})([.,)\s])".format(alias), replaceWithAlias, sqlstatement, flags=re.IGNORECASE | re.MULTILINE)

    return sqlstatement

def replaceWithAlias(matchobj):
    return "{}{{{}}}{}".format(matchobj.group(1), matchobj.group(2), matchobj.group(3))


def checkForJoin(comparisons):
    # print(comparisons)
    for item in comparisons:
        try:
            match1 = re.match('([\w$]+)\.([\w$]+)', item[0])
            match2 = re.match('([\w$]+)\.([\w$]+)', item[1])
            if match1.group(2) == match2.group(2):
                return True
        except:
            pass
    return False


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
