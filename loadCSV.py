import sys
import re
import csv

import mysql.connector
import mysql.connector.pooling

from lib.ConnectionLoader import ConnectionLoader
from lib import catdb
from lib import cfgProcessor

def parseCSV(csvname):
    csvfile = list()
    try:
        csvreader = open(csvname)
        readCSV = csv.reader(csvreader, delimiter=',')
        for row in readCSV:
            csvfile.append(tuple(row))
    except BaseException as e:
        print("Could not parse csv file.")
        print(str(e))
        csvfile = None

    # print("\ncsvfile (unsorted):") # COMMENT OUT
    # for x in csvfile: print(x) # COMMENT OUT

    return csvfile


def loadCSV(cataloginfo, numnodes, tablename, partitioninfo, partitionnodeinfo, csvfilename):
    # Get partition method and get list of connectionLoaders
    csvfile = parseCSV(csvfilename)

    if not cataloginfo or not tablename or not partitioninfo or not csvfile:
        print("loadCSV was not given the needed information to load the csv.")
        return False

    cparams = catdb.getCatalogParams(cataloginfo)
    if not cparams:
        print("Catalog info could not be processed into connection parameters from the cluster config.")
        return False

    tableinfo_list = catdb.queryTables(mysql.connector.connect(**cparams), tablename)

    if not tableinfo_list:
        print("Error in loadCSV: No tables found in the catalog with the given name '{}'.".format(tablename))
        return False

    if numnodes and len(tableinfo_list) != numnodes:
        print("Error in loadCSV: Catalog contains more nodes than specified in the cluster config.")
        return False


    if partitionnodeinfo:
        if len(tableinfo_list) != len(partitionnodeinfo) or len(tableinfo_list) != numnodes:
            print("Error in loadCSV: Catalog contains more nodes than specified in the cluster config.")
            return False

        for tableinfo in tableinfo_list:
            for pnodeinfo in partitionnodeinfo:
                if tableinfo['nodeid'] == pnodeinfo['nodeid']:
                    tableinfo['partparam1'] = pnodeinfo['param1']
                    tableinfo['partparam2'] = pnodeinfo['param2']

    for tableinfo in tableinfo_list:
        if partitioninfo['method'] == 'notpartition':
            tableinfo['partmtd'] = 0
        elif partitioninfo['method'] == 'range':
            tableinfo['partmtd'] = 1
        elif partitioninfo['method'] == 'hash':
            tableinfo['partmtd'] = 2
        else:
            print("Error in loadCSV: partition method give not one of the cases of 'notpartition', 'range', or 'hash'.")
            return False
        try:
            tableinfo['partcol'] = partitioninfo['column'] # Not needed if method is notpartition
        except:
            pass

    cat_cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "cat_cnxpool", pool_size = len(tableinfo_list), **cparams)
    conn_list = None

    partmtd = partitioninfo['method']
    if partmtd == 'notpartition':
        conn_list = noPartitioning(cat_cnxpool, tableinfo_list, csvfile)
    elif partmtd == 'range':
        conn_list = rangePartitioning(cat_cnxpool, tableinfo_list, csvfile)
    elif partmtd == 'hash':
        conn_list = hashPartitioning(cat_cnxpool, tableinfo_list, csvfile)

    if conn_list:
        # print("\nGot conn_list:") # COMMENT OUT
        # for conn in conn_list: # COMMENT OUT
        #     print("\nConnection Info:") # COMMENT OUT
        #     conn.show() # COMMENT OUT
        try:
            for conn in conn_list:
                conn.loadData()
            try:
                for conn in conn_list:
                    conn.commit()
                print("loadCSV: Tables successfully loaded.")
            except BaseException as e:
                print("Error in loadCSV when commiting:")
                print(str(e))
        except BaseException as e:
            print("Error in load CSV: Could not load Data:")
            print(str(e))
            for conn in conn_list:
                conn.rollback()
    else:
        print("Connection list could not be established.")

# No partitioning method so insert everything into all tables
def noPartitioning(cat_cnxpool, tableinfo_list, csvfile):
    conn_list = list()
    for tableinfo in tableinfo_list:
        catconn = cat_cnxpool.get_connection()
        nodeparams = catdb.getRowNodeParams(tableinfo)
        nodeconn = mysql.connector.connect(**nodeparams)

        conn_list.insert(-1, ConnectionLoader(catconn, nodeconn, tableinfo, csvfile) )

    return conn_list

# Range partitioning
def rangePartitioning(cat_cnxpool, tableinfo_list, csvfile):
    conn_list = list() # For storing connections.
    columns = getColumns(tableinfo_list[0]) # For figuring out which column number to range by.
    if not columns:
        return None

    colnum = None
    # Get column number for sorting
    for (i, column) in enumerate(columns):
        if column == tableinfo_list[0]['partcol']:
            colnum = i

    # sort csvfile
    csvfile = sorted(csvfile, key=lambda x: int(x[colnum]))

    # print("\ncsvfile (sorted):") # COMMENT OUT
    # for row in csvfile: print(row) # COMMENT OUT
    # print("\nCOLUMNS (where column '{}' is in position {}):\n{}".format(clustercfg['partition']['column'], colnum, columns)) # COMMENT OUT


    for tableinfo in tableinfo_list:
        # Get data in range
        # print("\nnode{}".format(node['nodeid'])) # COMMENT OUT
        # print("Range: {} to {}".format(clustercfg[str(node['nodeid'])]['param1'], clustercfg[str(node['nodeid'])]['param2'])) # COMMENT OUT
        if float(tableinfo['partparam1']) < float(tableinfo['partparam2']):
            (startrow, endrow) = getRangeSlice(
                                    float(tableinfo['partparam1']),
                                    float(tableinfo['partparam2']),
                                    colnum, csvfile
                                )
        else:
            (startrow, endrow) = (None, None)
        # print("Result ({}:{}) out of (0:{}):".format(startrow, endrow, len(csvfile))) # COMMENT OUT
        # for row in csvfile[startrow:endrow]: print(row) # COMMENT OUT
        if startrow is not None and endrow is not None:
            catconn = cat_cnxpool.get_connection()
            nodeparams = catdb.getRowNodeParams(tableinfo)
            nodeconn = mysql.connector.connect(**nodeparams)

            conn_list.insert(-1, ConnectionLoader(catconn, nodeconn, tableinfo, csvfile[startrow:endrow]) )
        else:
            return None

    return conn_list

# returns the beginning and ending index for slice for given range.
def getRangeSlice(low, high, colnum, csvfile):
    try:
        startrow = None
        endrow = None
        get_endrow = 0
        if low == '-inf':
            startrow = 0
            endrow = 0
            get_endrow = 1
        else:
            low = float(low)
        if high == '+inf':
            endrow = len(csvfile) - 1
            get_endrow = -1
        else:
            high = float(high)

        for (i, row) in enumerate(csvfile):
            if startrow is None and float(row[colnum]) > low:
                # print("{}>{}".format(row[colnum], low)) # COMMENT OUT
                startrow = i
                if get_endrow == 0:
                    endrow = i
                    get_endrow = 1
            elif get_endrow > 0 and float(row[colnum]) <= high:
                # print("{}<={}".format(row[colnum], high)) # COMMENT OUT
                endrow = i
        if endrow is not None:
            endrow = endrow + 1 # to include last element for slice command
        return (startrow, endrow)
    except BaseException as e:
        print("Problem with range parameters:")
        print(str(e))
        return (None, None)

# Hash partitioning
def hashPartitioning(cat_cnxpool, tableinfo_list, csvfile):
    conn_list = list()

    columns = getColumns(tableinfo_list[0]) # For figuring out which column number to range by.
    if not columns:
        return None

    colnum = None
    # Get column number for sorting
    for (i, column) in enumerate(columns):
        if column == tableinfo_list[0]['partcol']:
            colnum = i

    partparam1 = len(tableinfo_list)

    for tableinfo in tableinfo_list:
        catconn = cat_cnxpool.get_connection()
        nodeparams = catdb.getRowNodeParams(tableinfo)
        nodeconn = mysql.connector.connect(**nodeparams)

        hashedcsv = list()
        for row in csvfile:
            hashvalue = ((int(row[colnum]) % partparam1) +1)
            if tableinfo['nodeid'] == hashvalue:
                hashedcsv.insert(-1, row)

        conn_list.insert(-1, ConnectionLoader(catconn, nodeconn, tableinfo, hashedcsv))

    return conn_list

def getColumns(tableinfo):
    try:
        conn_params = catdb.getRowNodeParams(tableinfo)
        connection = mysql.connector.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM {};".format(tableinfo['tname']))
        column_names = [i[0] for i in cursor.description]
        return column_names
    except BaseException as e:
        print(cursor.statement)
        print("Could not get columns in loadCSV.getColumns()")
        print(str(e))
        print("Arg:")
        print(node)
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'cluster.cfg'
    if len(sys.argv) > 2:
        csvfilename = sys.argv[2]
    else:
        csvfilename = 'data.csv'

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.process(clustername)

    loadCSV(cataloginfo, numnodes, tablename, partitioninfo, partitionnodeinfo, csvfilename)
