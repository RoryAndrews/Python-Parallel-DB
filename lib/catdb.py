import mysql.connector
import mysql.connector.pooling
import re

def makeDtables(catalogconn):
    try:
        dtables = (
            "CREATE TABLE "
            "DTABLES(tname char(32), "
            "nodedriver char(64), "
            "nodeurl char(128), "
            "nodeuser char(16), "
            "nodepasswd char(16), "
            "partmtd int, "
            "nodeid int, "
            "partcol char(32), "
            "partparam1 char(32), "
            "partparam2 char(32));"
        )
        cursor = catalogconn.cursor()
        cursor.execute(dtables)
        catalogconn.commit()
    except mysql.connector.ProgrammingError:
        pass
    except BaseException as e:
        print("Error in catdb.makeDtables(): {}".format(str(e)))
    finally:
        cursor.close()
        catalogconn.close()

def insertTable(catalogconn, tableinfo):
    query = (
        "INSERT INTO DTABLES"
        "(tname, nodedriver, nodeurl, nodeuser, nodepasswd, "
        "partmtd, nodeid, partcol, partparam1, partparam2) "
        "VALUES (%(tname)s, %(nodedriver)s, %(nodeurl)s, %(nodeuser)s, %(nodepasswd)s, NULL, %(nodeid)s, NULL, NULL, NULL);"
    )
    result = False

    try:
        cursor = catalogconn.cursor()
        cursor.execute(query, tableinfo)
        catalogconn.commit()
        result = True
    # except mysql.connection.Error as e:
    #     print("Error inserting row into dtables:")
    #     print(e)
    #     print("For row:")
    #     print(tableinfo)
    except BaseException as e:
        print(str(e))
        print("Error inserting row into dtables for row: {}".format(tableinfo))
    finally:
        cursor.close()
        catalogconn.close()
        return result

def removeByTable(catalogconn, tableinfo):
    query = "DELETE FROM DTABLES WHERE tname=%(tname)s;"
    result = False

    try:
        cursor = catalogconn.cursor()
        cursor.execute(query, tableinfo)
        catalogconn.commit()
        result = True
    # except mysql.connection.Error as e:
    #     print("Error removing rows from dtables:")
    #     print(e)
    #     print("For tableinfo (rows containing tname):")
    #     print(tableinfo)
    except BaseException as e:
        print(str(e))
        print("Error removing rows from dtables:")
        print("For tableinfo (rows containing tname): {}".format(tableinfo))
    finally:
        cursor.close()
        catalogconn.close()
        return result

def partitionUpdate(catalogconn, tableinfo):
    update_catalog = (
        "UPDATE DTABLES "
        "SET partmtd=%(partmtd)s, "
        "partcol=%(partcol)s, "
        "partparam1=%(partparam1)s, "
        "partparam2=%(partparam2)s "
        "WHERE tname=%(tname)s AND nodeid=%(nodeid)s;"
    )
    result = False

    try:
        cursor = catalogconn.cursor()
        cursor.execute(update_catalog, tableinfo)
        catalogconn.commit()
        result = True
    # except mysql.connector.Error as err:
    #     print("Error updating catalog row:")
    #     print(err)
    #     print("For row:")
    #     print(tableinfo)
    except BaseException as err:
        print(str(err))
        print("Error updating catalog row for row: {}".format(tableinfo))
    finally:
        cursor.close()
        catalogconn.close()
        return result

# Used to find rows containing matching tname
def queryTables(catalogconn, tname):
    catalog_query = (
        "SELECT * "
        "FROM DTABLES "
        "WHERE tname = %s;"
    )

    try:
        cursor = catalogconn.cursor(dictionary=True)
        cursor.execute(catalog_query, (tname,))
        results = cursor.fetchall()
    # except mysql.connector.Error as err:
    #     print("Error querying tables:")
    #     print(err)
    #     print("For row:")
    #     print(tableinfo)
    except BaseException as err:
        print(str(err))
        print("Error querying tables for row: {}".format(tableinfo))
    finally:
        cursor.close()
        catalogconn.close()

    if len(results) > 0:
        return results
    else:
        return None

def getCatalogParams(cataloginfo):
    try:
        (host, port, database) = parseURL(cataloginfo['hostname'])
        return  {
            'host': host,
            'port': port,
            'database': database,
            'user': cataloginfo['username'],
            'password': cataloginfo['passwd']

        }
    except:
        return None

def getNodeParams(nodeinfo):
    return getCatalogParams(nodeinfo)

def getRowNodeParams(dtablerow):
    try:
        (host, port, database) = parseURL(dtablerow['nodeurl'])
        return  {
            'host': host,
            'port': port,
            'database': database,
            'user': dtablerow['nodeuser'],
            'password': dtablerow['nodepasswd']

        }
    except:
        return None

# Grabs the address, port, and database from the hostname url.
def parseURL(url):
    hostmatch = re.search('^.*//([\.\d]+):(\d+)/(.*)$', url, flags=re.IGNORECASE)
    if hostmatch and len(hostmatch.groups()) == 3:
        return hostmatch.groups()
    else:
        return None

if __name__ == "__main__":
    clustercfg = {
        'hostname': "jdbc:db2://127.0.0.1:3306/testdb",
        'username': "dbuser",
        'passwd': "mypasswd"
    }
    print("\nclustercfg:")
    print(clustercfg)

    # Test parseURL
    print("\nparseURL:")
    print(parseURL(clustercfg['hostname']))

    # Test getCatalogParams
    print("\ngetCatalogParams:")
    cparams = getCatalogParams(clustercfg)

    cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cnxpool", pool_size = 3, **cparams)
    conn = cnxpool.get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS DTABLES;")
    print(cursor.fetchone())
    cursor.close()
    conn.close()

    row1 = {
        'tname': "BOOKS",
        'nodedriver': "test",
        'nodeurl': "jdbc:db2://127.0.0.1:3306/testdb",
        'nodeuser': "dbuser",
        'nodepasswd': "mypasswd",
        'partmtd': 0,
        'nodeid': 1,
        'partcol': "age",
        'partparam1': 0,
        'partparam2': 10
    }
    row2 = {
        'tname': "BOOKS",
        'nodedriver': "test",
        'nodeurl': "jdbc:db2://127.0.0.1:3306/testdb2",
        'nodeuser': "dbuser",
        'nodepasswd': "mypasswd",
        'partmtd': 0,
        'nodeid': 2,
        'partcol': "age",
        'partparam1': 10,
        'partparam2': 20
    }


    # Test makeDtables
    input("makeDtables: press ENTER")

    makeDtables(cnxpool.get_connection())

    # Test insertTable
    input("insertTable: press ENTER for row1")
    insertTable(cnxpool.get_connection(), row1)
    input("insertTable: press ENTER for row2")
    insertTable(cnxpool.get_connection(), row2)

    # Test partitionUpdate
    input("partitionUpdate: press ENTER for row1")
    partitionUpdate(cnxpool.get_connection(), row1)
    input("partitionUpdate: press ENTER for row2")
    partitionUpdate(cnxpool.get_connection(), row2)

    # Test queryTables
    input("queryTables: press ENTER")
    print(queryTables(cnxpool.get_connection(), row1["tname"]))

    # Test removeByTable
    input("removeByTable: press ENTER")
    removeByTable(cnxpool.get_connection(), row1)
