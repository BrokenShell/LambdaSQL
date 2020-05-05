"""
MongoDB was way easier in general, once it's setup.
It does take a little longer to setup though.
"""
from pymongo import MongoClient
import sqlite3 as sql


conn = sql.connect("rpg_db.sqlite3")
curs = conn.cursor()
characters = curs.execute(
    "SELECT * FROM charactercreator_character"
).fetchall()

keys = (
    'name', 'level', 'exp', 'hp', 'strength',
    'intelligence', 'dexterity', 'wisdom',
)

db = MongoClient(
    "mongodb+srv://brokenshell:<PASSWORD>@cluster0-xz3sf.mongodb.net/test?retryWrites=true&w=majority"
).rpg_db.characters

db.insert_many(
    {k: v for k, v in zip(keys, char[1:])} for char in characters
)

print(*db.characters.find(), sep='\n')
"""
Stretch Goal: See MonsterData
I built almost everything that went into this:
    Storm.hpp 
    Fortuna.py 
    MonsterFactory.py
https://colab.research.google.com/drive/1Sm4uCSAbo-TwI-BX1SRWiBfzk9AFXqfy
"""
