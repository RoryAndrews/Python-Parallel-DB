import sys
from lib import ConnectionLoader

def processSQL(cataloginfo, numnodes, nodeinfo, sqlfilename):
    print (cataloginfo, numnodes, nodeinfo, sqlfilename)
    
if __name__ =="__main__":
    catalog = {
        'driver' : 'com.ibm.db2.jcc.DB2Driver',
        'hostname' : 'jdbc:db2://127.0.0.1:3306/testdb',
        'username' : 'dbuser',
        'passwd' : 'mypasswd',
    }

    numnodes = 2

    nodeinfo = {
        'nodeid' : '1',
        'driver' : 'com.ibm.db2.jcc.DB2Driver',
        'hostname' : 'jdbc:db2://127.0.0.1:3306/testdb',
        'username' : 'dbuser',
        'passwd' : 'mypasswd',
    }

    sqlfilename = "process_sqlfile"

    processSQL(catalog,numnodes,nodeinfo,sqlfilename)
