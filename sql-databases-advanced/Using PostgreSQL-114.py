## 3. Psycopg2 ##

import psycopg2
conn=psycopg2.connect('dbname=dq user=dq')
cursor=conn.cursor()
print(cursor)
conn.close()

## 4. Creating a table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
c='''
CREATE TABLE notes (
id INTEGER,
body TEXT,
title TEXT
);
'''
cur.execute(c)
conn.close()

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
c='''
CREATE TABLE notes (
id INTEGER,
body TEXT,
title TEXT
);
'''
cur.execute(c)
conn.commit()
conn.close()



## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit=True
c='''
CREATE TABLE facts (
id INTEGER PRIMARY KEY,
country TEXT,
value TEXT
);
'''
cur.execute(c)
conn.close()


## 7. Executing queries ##

conn=psycopg2.connect('dbname=dq user=dq')
c='''
INSERT INTO notes
VALUES (1,'Do more missions on Dataquest.','Dataquest reminder');
'''
cur=conn.cursor()
cur.execute(c)
q="SELECT * FROM notes;"
cur.execute(q)
rows=cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn=psycopg2.connect('dbname=dq user=dq')
conn.autocommit=True
cur=conn.cursor()
c='''
CREATE DATABASE income OWNER dq;
'''
cur.execute(c)
conn.close()

## 9. Deleting a database ##

conn=psycopg2.connect('dbname=dq user=dq')
conn.autocommit=True
c="DROP DATABASE income;"
cur=conn.cursor()
cur.execute(c)
conn.close()