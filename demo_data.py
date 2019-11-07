import sqlite3
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# The 2 below code queries were ran only once to avoid duplicating rows 

# query = """CREATE TABLE demo (
# s varchar(20),x int,y int
# );"""
# curs.execute(query)
# curs.fetchall()
#
# # s ('g', 'v', 'f'), x (3, 5, 8), y (9, 7, 7)
# query1 = """INSERT INTO demo (s, x, y)
# VALUES ('g', 3, 9)"""
# query2 = """INSERT INTO demo (s, x, y)
# VALUES ('v', 5, 7)"""
# query3 = """INSERT INTO demo (s, x, y)
# VALUES ('f', 8, 7)"""
# curs.execute(query1)
# curs.execute(query2)
# curs.execute(query3)
# insert_curs = curs.fetchall()
# print("Insert values: ", insert_curs)

query = """SELECT * FROM demo"""
curs.execute(query)
tab = curs.fetchall()
print("Our table: ", tab)

# commit
conn.commit()

# How many rows
query = """SELECT COUNT(*)
FROM demo"""
curs.execute(query)
demo_rows = curs.fetchall()
print("Rows in demo: ", demo_rows)

# How many rows are at least 5 in X and Y
query = """SELECT COUNT(*)
FROM demo
WHERE (x) >= 5"""
curs.execute(query)
fiverX = curs.fetchall()
print("for X: ", fiverX)

query = """SELECT COUNT(*)
FROM demo
WHERE (y) >= 5"""
curs.execute(query)
fiverY = curs.fetchall()
print("for Y: ", fiverX)

# How many unique values in y

query = """SELECT COUNT(DISTINCT y)
FROM demo"""
curs.execute(query)
dy = curs.fetchall()
print("Unique values of y: ", dy)

