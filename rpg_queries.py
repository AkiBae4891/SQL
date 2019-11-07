import pandas as pd
from sqlalchemy import create_engine
import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

query = """SELECT * 
FROM charactercreator_character 
INNER JOIN charactercreator_mage 
ON character_id = character_ptr_id;"""

curs.execute(query)
results = curs.fetchone()
remaining_results = curs.fetchall()

print(results)
print(remaining_results)

'''
How many total characters?
There are 302 characters
'''

query = """SELECT COUNT(character_id) FROM charactercreator_character;"""
curs.execute(query)
curs.fetchall()

'''
How many of each specific Subclass
'''

# Cleric
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_cleric;"""
cleric = curs.execute(query)
curs.fetchall()
print("The amount of Clerics: ", cleric)

# Fighter
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_fighter;"""
fighter = curs.execute(query)
curs.fetchall()
print("The amount of fighters: ", fighter)

# Mage
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_mage;"""
mage = curs.execute(query)
curs.fetchall()
print("The amount of mages: ", mage)

# Necromancer
query = """SELECT COUNT(mage_ptr_id) 
FROM charactercreator_necromancer;"""
necro = curs.execute(query)
curs.fetchall()
print("The amount of necros: ", necro)

# Thief
query = """SELECT COUNT(character_ptr_id) 
FROM charactercreator_thief;"""
thief = curs.execute(query)
curs.fetchall()
print("The amount of thieves: ", thief)

'''
How many total Items?
'''

query = """SELECT COUNT(item_id)
FROM armory_item"""
total_items = curs.execute(query)
curs.fetchall()
print("Total items: ", total_items)

'''
How many of the Items are weapons? How many are not?
'''

# add up all items, add up weapons, then subtract weapons. Easy solution
query1 = """SELECT COUNT(item_id)
FROM armory_item"""
q1 = curs.execute(query1)
curs.fetchall()
print("Items: ", q1)

query2 = """SELECT COUNT(item_ptr_id)
FROM armory_weapon"""
q2 = curs.execute(query2)
curs.fetchall()
print("Weapons: ", q2)

'''
How many Items does each character have? (Return first 20 rows)
How many weapons does each character have? (Return first 20 rows)
'''

query = """SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
GROUP BY character_id LIMIT 20;"""
char_item = curs.execute(query)
curs.fetchall()
print("Items each Character has: ", char_item)

query = """SELECT character_id, COUNT(item_id)
FROM charactercreator_character_inventory
WHERE item_id > 138
GROUP BY character_id;"""
char_weap = curs.execute(query)
curs.fetchall()
print("Weapons each Character has: ", char_weap)

'''
On average, how many Items does each Character have?
On average, how many weapons does each Character have?
Answer is: 898 / 302 = 2.97
'''

# using division

query = """SELECT COUNT(item_id) / COUNT(DISTINCT character_id)
FROM charactercreator_character_inventory;"""
avg_items = curs.execute(query)
curs.fetchall()
print("Average items each character has: ", avg_items)

# using division
query = """SELECT COUNT(item_id) / COUNT(DISTINCT character_id)
FROM charactercreator_character_inventory
WHERE item_id > 138"""
avg_weap = curs.execute(query)
curs.fetchall()
print("Average weapons each character has: ", avg_weap)
