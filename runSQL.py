from lib.cfgProcessor import cfgProcessor
from csvLoader import csvLoader


if __name__ =="__main__":
    if len(sys.argv) > 1:
        clustername = sys.argv[1]
    else:
        clustername = 'clustercfg'
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = None

    (cataloginfo, numnodes, nodeinfo, tablename, partitioninfo, partitionnodeinfo) = cfgProcessor.processCfg(clustername)
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
            csvLoader.loadCSV(
                cataloginfo=cataloginfo, numnodes=numnodes, tablename=tablename,
                partitioninfo=partitioninfo, partitionnodeinfo=partitionnodeinfo,
                csvfilename=filename
            )
        else:
            processSQL(cataloginfo=cataloginfo, numnodes=numnodes, nodeinfo=nodeinfo, sqlfilename=filename)
    else:
        print("ERROR: Cluster configuration file could not be used.")
