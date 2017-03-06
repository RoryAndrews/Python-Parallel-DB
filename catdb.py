import mysql.connector
import re

def makeDtables(catalogparams):
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

        connection = mysql.connector.connect(**catalogparams)
        cursor = connection.cursor()
        cursor.execute(dtables)
        connection.commit()
    except:
        pass

def insertTable(catalogparams, tableinfo):
    query = (
        "INSERT INTO DTABLES"
        "(tname, nodedriver, nodeurl, nodeuser, nodepasswd, "
        "partmtd, nodeid, partcol, partparam1, partparam2) "
        "VALUES (%(tname)s, %(nodedriver)s, %(nodeurl)s, %(nodeuser)s, %(nodepasswd)s, NULL, %(nodeid)s, NULL, NULL, NULL);"
    )

    try:
        connection = mysql.connector.connect(**catalogparams)
        cursor = connection.cursor()
        cursor.execute(query, tableinfo)
        connection.commit()
    # except mysql.connection.Error as e:
    #     print("Error inserting row into dtables:")
    #     print(e)
    #     print("For row:")
    #     print(tableinfo)
    except BaseException as e:
        print("Error inserting row into dtables:")
        print(str(e))
        print("For row:")
        print(tableinfo)
    finally:
        cursor.close()
        connection.close()

def removeByTable(catalogparams, tableinfo):
    query = "DELETE FROM DTABLES WHERE tname=%(tname)s;"

    try:
        connection = mysql.connector.connect(**catalogparams)
        cursor = connection.cursor()
        cursor.execute(query, tableinfo)
        connection.commit()
    except mysql.connection.Error as e:
        print("Error removing rows from dtables:")
        print(e)
        print("For tableinfo (rows containing tname):")
        print(tableinfo)
    except BaseException as e:
        print("Error removing rows from dtables:")
        print(str(e))
        print("For tableinfo (rows containing tname):")
        print(tableinfo)
    finally:
        cursor.close()
        connection.close()

def partitionUpdate(catalogparams, tableinfo):
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
        connection = mysql.connector.connect(**catalogparams)
        cursor = connection.cursor()
        cursor.execute(update_catalog, tableinfo)
        connection.commit()
        result = True
    except mysql.connector.Error as err:
        print("Error updating catalog row:")
        print(err)
        print("For row:")
        print(tableinfo)
    except BaseException as err:
        print("Error updating catalog row:")
        print(str(err))
        print("For row:")
        print(tableinfo)
    finally:
        cursor.close()
        connection.close()
    return result

def queryTables(catalogparams, tableinfo):
    catalog_query = (
        "SELECT * "
        "FROM DTABLES "
        "WHERE tname = %(tname)s;"
    )

    try:
        connection = mysql.connector.connect(**catalogparams)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(catalog_query, tableinfo)
        results = cursor.fetchall()

    except mysql.connector.Error as err:
        print("Error querying tables:")
        print(err)
        print("For row:")
        print(tableinfo)
    except BaseException as err:
        print("Error querying tables:")
        print(str(err))
        print("For row:")
        print(tableinfo)
    finally:
        cursor.close()
        connection.close()

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
                    'user': clustercfg['username'],
                    'password': clustercfg['passwd']

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

    connection = mysql.connector.connect(**cparams)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS DTABLES;")

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

    makeDtables(cparams)

    # Test insertTable
    input("insertTable: press ENTER for row1")
    insertTable(cparams, row1)
    input("insertTable: press ENTER for row2")
    insertTable(cparams, row2)

    # Test partitionUpdate
    input("partitionUpdate: press ENTER for row1")
    partitionUpdate(cparams, row1)
    input("partitionUpdate: press ENTER for row2")
    partitionUpdate(cparams, row2)

    # Test queryTables
    input("queryTables: press ENTER")
    print(queryTables(cparams, row1))

    # Test removeByTable
    input("removeByTable: press ENTER")
    removeByTable(cparams, row1)
