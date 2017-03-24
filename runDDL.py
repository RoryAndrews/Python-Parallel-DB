import sys
import re
import io
import mysql.connector
import mysql.connector.pooling

from lib.ConnectionThread import ConnectionThread
from lib import catdb

def runDDL(cataloginfo, numnodes, nodeinfo, ddlfilename):
    if not cataloginfo or not numnodes or not nodeinfo or not ddlfilename:
        print("runDDL was not given the needed information to run the ddl.")
        return False

    cparams = catdb.getCatalogParams(cataloginfo)
    if not cparams:
        print("Catalog info could not be processed into connection parameters from the cluster config.")
        return False

    cat_cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cat_cnxpool", pool_size = len(nodeinfo), **cparams)
    catdb.makeDtables(cat_cnxpool.get_connection())
    ddlfile = open(ddlfilename,'r')
    ddl = ddlfile.read()
    ddlfile.close()
    tname = re.search("table (\w+)", ddl, flags=re.IGNORECASE | re.MULTILINE).group(1)

    threads = list()

    for (i, node) in enumerate(nodeinfo):
        catconn = cat_cnxpool.get_connection()
        nodeparams = catdb.getNodeParams(node)
        nodeconn = mysql.connector.connect(**nodeparams)

        dtablerow = {
            'tname': tname,
            'nodedriver': node['driver'],
            'nodeurl': node['hostname'],
            'nodeuser': node['username'],
            'nodepasswd': node['passwd'],
            'partmtd': None,
            'nodeid': node['nodeid'],
            'partcol': None,
            'partparam1': None,
            'partparam2': None
        }

        threads.insert( -1, ConnectionThread(i+1, catconn, nodeconn, ddl, ddlfilename, dtablerow))

    for conn in threads:
        conn.run()


if __name__ == "__main__":
    from lib import cfgProcessor

    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'cluster.cfg'
    if len(sys.argv) > 2:
        ddlfilename = sys.argv[2]
    else:
        ddlfilename = 'table.ddl'

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)

    # cparams = catdb.getCatalogParams(cataloginfo)
    # conn = mysql.connector.connect(**cparams)
    # cursor = conn.cursor()
    # cursor.execute("DROP DATABASE jesusrorycatalog;")
    # cursor.execute("DROP DATABASE jesusrory1;")
    # cursor.execute("DROP DATABASE jesusrory2;")
    # cursor.execute("CREATE DATABASE jesusrorycatalog;")
    # cursor.execute("CREATE DATABASE jesusrory1;")
    # cursor.execute("CREATE DATABASE jesusrory2;")
    # cursor.close()
    # conn.close()
    # conn = mysql.connector.connect(**cparams)
    # catdb.makeDtables(conn)

    runDDL(cataloginfo, numnodes, nodeinfo, ddlfilename)
