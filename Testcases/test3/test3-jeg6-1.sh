./test3-jeg6-1.pre
python3 runSQL.py test3-jeg6-1-load.cfg test3-jeg6-1.sql
python3 runSQL.py test3-jeg6-1.cfg orders-test-data.csv | sort > test3-jeg6-1.out
./test3-jeg6-1.post | sort > test3-jeg6-1.post.out
diff -b ./test3-jeg6-1.post.out ./test3-jeg6-1.post.exp
#Cleanup
python3 runSQL.py test3-jeg6-1-load.cfg test3-jeg6-1.pre.sql
