SELECT Sailors.sname
FROM Sailors, Reserves
WHERE Sailors.sid=Reserves.sid and Reserves.day='2009-12-21'
;
