./test1-jeg6-1.pre
python3 runSQL.py test1-jeg6-1.cfg test1-jeg6-1.ddl | sort > test1-jeg6-1.out
./test1-jeg6-1.post | sort > test1-jeg6-1.post.out
diff ./test1-jeg6-1.post.out ./test1-jeg6-1.post.exp
#Cleanup
python3 runSQL.py test1-jeg6-1.cfg test1-jeg6-1.pre.ddl
