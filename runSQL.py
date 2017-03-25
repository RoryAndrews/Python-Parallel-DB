import sys
import re

from processSQL import *
from lib import cfgProcessor
from loadCSV import *
from runDDL import *
from lib.PartitionJoinThread import PartitionJoinThread


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
    if not cparams:
        print("runSQL: Catalog info invalid.")
        return False
    if len(aliases) > 2:
        print("runSQL: More than two tables in a query is not allowed.")
        return False
    elif len(aliases) < 2:
        print("runSQL: Can't perform a join with one Table.")
        return False

    tableM = aliases[0][0]
    tableN = aliases[1][0]
    conn = mysql.connector.connect(**cparams)
    tableinfoM = catdb.queryTables(conn, tableM)
    conn = mysql.connector.connect(**cparams)
    tableinfoN = catdb.queryTables(conn, tableN)

    plan = getQueryPlan(tableM, tableN, tableinfoM, tableinfoN)
    print("plan: {}".format(plan))

    if not plan:
        print("runSQL: Failed to generate plan.")
        return False

    partitionedsql = getPartitionedQuery(sqlstatement, aliases, columns)
    print(partitionedsql)

    if len(tableinfoM) > len(tableinfoN):
        node_cnxpool_list = list(None for x in range(len(tableinfoM)))
        for tableinfo in tableinfoM:
            nodeid = int(tableinfo['nodeid'])
            nparams = catdb.getRowNodeParams(tableinfo)
            node_cnxpool_list[nodeid - 1] = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cnxpool{}".format(nodeid - 1), pool_size = len(plan), **nparams)
    else:
        node_cnxpool_list = list(None for x in range(len(tableinfoN)))
        for tableinfo in tableinfoN:
            nodeid = int(tableinfo['nodeid'])
            nparams = catdb.getRowNodeParams(tableinfo)
            node_cnxpool_list[nodeid - 1] = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cnxpool{}".format(nodeid - 1), pool_size = len(plan), **nparams)

    print(node_cnxpool_list)

    threadlist = list()
    for (i,step) in enumerate(plan):
        m = step[0][0]
        n = step[0][1]
        threadlist.append(PartitionJoinThread(
                                        threadID=i, plan=step,
                                        tableM=tableM, tableM_connection=node_cnxpool_list[m].get_connection(),
                                        tableN=tableN, tableN_connection=node_cnxpool_list[n].get_connection(),
                                        columns=columns, partitionedsql=partitionedsql,
                                        sqlfilename=sqlfilename))

    for thread in threadlist:
        print(thread)
        print(thread.plan)
        print(thread.tableM)
        print(thread.tableM_connection.server_host)
        print(thread.tableN)
        print(thread.tableN_connection.server_host)
        print(thread.columns)




# Returns string where
def getPartitionedQuery(sqlstatement, aliases, columns):
    regexstring = "([\s\W])({})([\s\W])"
    for (i, (table, alias)) in enumerate(aliases):
        if not alias:
            # Replace tablename with a format variable containing index number
            sqlstatement = re.sub(regexstring.format(table), replaceWithAlias, sqlstatement, flags=re.IGNORECASE | re.MULTILINE)
            sqlstatement = re.sub("{{{}}}".format(table), "{{{}}}".format(i), sqlstatement, flags=re.IGNORECASE | re.MULTILINE)
        else:
            # Filter out tablename and then replace alias with a format variable containing index number
            sqlstatement = re.sub(regexstring.format(table), replaceWithAlias, sqlstatement, flags=re.IGNORECASE | re.MULTILINE)
            sqlstatement = re.sub("{{{}}}".format(table), "", sqlstatement, flags=re.IGNORECASE | re.MULTILINE)
            sqlstatement = re.sub(regexstring.format(alias), replaceWithAlias, sqlstatement, flags=re.IGNORECASE | re.MULTILINE)
            sqlstatement = re.sub("{{{}}}".format(alias), "{{{}}}".format(i), sqlstatement, flags=re.IGNORECASE | re.MULTILINE)

    return sqlstatement

def replaceWithAlias(matchobj):
    return "{}{{{}}}{}".format(matchobj.group(1), matchobj.group(2), matchobj.group(3))

# Generates a plan for joining all partitions.
# Format is a list of ((m,n), d)
# where m and n is the index of the table partition in tableinfo being joined
# and where d is the direction a partition needs to be transferred
# (-1 means partition in node n -> m, 1 is m -> n, and 0 is no transfer)
def getQueryPlan(tableM, tableN, tableinfoM, tableinfoN):
    numOfM = len(tableinfoM)
    numOfN = len(tableinfoN)

    tableinfoM = sorted(tableinfoM, key=lambda x: int(x['nodeid']))
    tableinfoN = sorted(tableinfoN, key=lambda x: int(x['nodeid']))

    plan = list()

    joinlist = list()
    for m in range(numOfM):
        for n in range(numOfN):
            joinlist.append((m,n))

    nodeload = list(0 for x in range(max(numOfM, numOfN)))
    for join in joinlist:
        m = join[0]
        n = join[1]
        m_nodeID = int(tableinfoM[m]['nodeid'])
        n_nodeID = int(tableinfoN[n]['nodeid'])
        if m_nodeID == n_nodeID:
            nodeload[m_nodeID - 1] += 1
            plan.append(((m,n), 0))
            # print("join: {} load: {}".format(((m,n), 0), nodeload))

    for join in joinlist:
        m = join[0]
        n = join[1]
        m_nodeID = int(tableinfoM[m]['nodeid'])
        n_nodeID = int(tableinfoN[n]['nodeid'])
        if m_nodeID != n_nodeID:
            if nodeload[m_nodeID - 1] > nodeload[n_nodeID - 1]:
                nodeload[n_nodeID - 1] += 1
                transferdirection = 1
            elif nodeload[m_nodeID - 1] < nodeload[n_nodeID - 1]:
                nodeload[m_nodeID - 1] += 1
                transferdirection = -1
            else:
                if m_nodeID > n_nodeID:
                    nodeload[m_nodeID - 1] += 1
                    transferdirection = -1
                else:
                    nodeload[n_nodeID - 1] += 1
                    transferdirection = 1
            plan.append(((m,n), transferdirection))
            # print("join: {} load: {}".format(((m,n), transferdirection), nodeload))
    print("node load: {}".format(nodeload))
    return plan



def checkForJoin(comparisons):
    # print(comparisons)
    for item in comparisons:
        try:
            match1 = re.match('([\w$]+)\.([\w$]+)', item[0])
            match2 = re.match('([\w$]+)\.([\w$]+)', item[1])
            if match1 and match2:
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
        # filetype = filename.split(".")
    else:
        print("Not enough arguements given.")
        quit()

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)
    # try:
    #     if filetype[1] == "ddl":
    #         (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)
    #         runDDL(cataloginfo, numnodes, nodeinfo, filename)
    #         quit()
    # except:
    #     pass
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
