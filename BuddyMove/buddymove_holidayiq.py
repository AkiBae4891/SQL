import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Buddymove Dataset; Assignment 2


df = pd.read_csv('buddymove_holidayiq.csv')
print("Shape of DF:", df.shape)
print(df.head())

# make buddymove_holidayiq.sqlite3 db
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

# Create in memory SQLite db
engine = create_engine('sqlite://', echo=False)

df.to_sql('buddymove_holidayiq', con=engine, if_exists='replace', index_label='id')
fetch = engine.execute("SELECT * FROM buddymove_holidayiq").fetchall()
print(fetch)

query = """SELECT COUNT(*)
FROM budymove_holidayiq"""
curs.execute(query)
count = curs.fetchall()
print("The number of rows in db: ", count)

query = """SELECT COUNT(User Id) ....."""
curs.execute(query)
reviews = curs.fetchall()
print("How many reviewed at least 100: ", reviews)