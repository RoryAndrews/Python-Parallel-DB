./test2-jeg6-1.pre
python3 runDDL.py test2-jeg6-1-load.cfg test2-jeg6-1.sql
python3 runSQL.py test2-jeg6-1.cfg orders-test-data.csv | sort > test2-jeg6-1.out
./test2-jeg6-1.post | sort > test2-jeg6-1.post.out
diff ./test2-jeg6-1.post.out ./test2-jeg6-1.post.exp
#Cleanup
python3 runDDL.py test2-jeg6-1-load.cfg test2-jeg6-1.pre.sql
