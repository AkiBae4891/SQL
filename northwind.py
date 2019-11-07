import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# read available tables
query = """SELECT name 
FROM sqlite_master 
WHERE type='table' 
ORDER BY name;"""
curs.execute(query)
table_avail = curs.fetchall()
print("Tables available: ", table_avail)

# See schema
query = """SELECT sql 
FROM sqlite_master 
WHERE name = 'Customer'"""
curs.execute(query)
schema = curs.fetchall()
print("Schema used: ", schema)

# What are the ten most expensive items (per unit price) in the database?
query = """SELECT ProductName, UnitPrice 
FROM Product 
ORDER BY UnitPrice DESC
LIMIT 10;"""
curs.execute(query)
top_ten = curs.fetchall()
print("Top ten expensive items: ", top_ten)

# Average age of Employees at time of hiring
query = """SELECT AVG(HireDate - BirthDate)
FROM Employee """
curs.execute(query)
avg_age = curs.fetchall()
print("Avg age of employees at hiring :", avg_age)

# STRETCH GOAL: Looks like cites in Washington State hires older people
query = """SELECT AVG(HireDate - BirthDate), City
FROM Employee 
GROUP BY City"""
curs.execute(query)
stretch = curs.fetchall()
print("Ages hired vary by city: ", stretch)

# What are the ten most expensive items (per unit price) in the database AND their Supplier?
# Join Product and Supplier on Id and Id. (Note: I asked TL why Cote de Blaye not in this list, but in previous) Unsure.
query = """SELECT ProductName, UnitPrice, CompanyName
FROM Product
JOIN Supplier
ON Product.Id = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;"""
curs.execute(query)
top_ten_sup = curs.fetchall()
print("Top ten expensive items and suppliers: ", top_ten_sup)

# What is the largest category (by number of unique products in it)
# Confections is the largest with 13 products 
query = """SELECT CategoryName, COUNT(Product.Id)
FROM Category
INNER JOIN Product
ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY COUNT(Product.Id) DESC 
LIMIT  3;"""
curs.execute(query)
cat = curs.fetchall()
print("Largest category is: ", cat)

# Who is the employee with the most territory
# Robert has 10 territories

query = """SELECT Employee.FirstName, COUNT(TerritoryId)
FROM EmployeeTerritory
INNER JOIN Employee
ON EmployeeTerritory.EmployeeId = Employee.Id
GROUP BY Employee.Id
ORDER BY COUNT(TerritoryId) DESC 
LIMIT  3;"""
curs.execute(query)
T = curs.fetchall()
print("The employee with the most territories is: ", T)
