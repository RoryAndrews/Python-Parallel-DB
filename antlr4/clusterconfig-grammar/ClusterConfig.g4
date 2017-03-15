grammar ClusterConfig;

config: stat+ ;

stat: catalog_info
    | node_info
    | partition_info
    | numnodes
    | tablename
    ;

catalog_info: 'catalog' DOT key EQUALS value ;

node_info: 'partition' DOT 'node' nodeid DOT key EQUALS value ;

partition_info: 'partition' DOT key EQUALS value ;

numnodes: 'numnodes' EQUALS NUM+ ;

tablename: 'tablename' EQUALS key ;

nodeid: NUM+ ;
key: (CHARS | NUM)+ ;
value: (PLUS | MINUS | CHARS | NUM | DOT | SLASH | COLON | UNDERSCORE)+ ;

COLON: ':' ;
SLASH: '/' ;
EQUALS: '=' ;
DOT: '.' ;
UNDERSCORE: '_' ;
PLUS: '+' ;
MINUS: '-' ;
NUM: ( '0' .. '9' )+ ;
CHARS: ( 'a' .. 'z' | 'A' .. 'Z')+ ;
WS: [ \t\r\n]+ -> skip ;
