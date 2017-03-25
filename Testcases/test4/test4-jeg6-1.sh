./test4-jeg6-1.pre
python3 runSQL.py test4-jeg6-1-load.cfg test4-jeg6-1.sql
python3 runSQL.py test4-jeg6-1-load.cfg test4-jeg6-1-2.sql

python3 runSQL.py test4-jeg6-1.cfg orders-test-data.csv | sort > test4-jeg6-1.out
python3 runSQL.py test4-jeg6-1-2.cfg customers-test-data.csv | sort > test4-jeg6-1-2.out
python3 runSQL.py test4-jeg6-1-catalog.cfg test4-jeg6-1.post.1.sql | sort > test4-jeg6-1-join.out

./test4-jeg6-1.post | sort > test4-jeg6-1.post.out
diff -b ./test4-jeg6-1.post.out ./test4-jeg6-1.post.exp

#Cleanup
python3 runSQL.py test4-jeg6-1-load.cfg test4-jeg6-1.pre.sql
python3 runSQL.py test4-jeg6-1-load.cfg test4-jeg6-1.pre-2.sql
