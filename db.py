import sqlite3

conn = sqlite3.connect("spend.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE users (
    uid integer PRIMARY KEY AUTOINCREMENT, 
    email text NOT NULL UNIQUE,
    uname text NOT NULL,
    name text NOT NULL,
    pswd text NOT NULL
)"""
cursor.execute(sql_query)