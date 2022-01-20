import sqlite3

conn = sqlite3.connect("spend.sqlite")

cursor = conn.cursor()
sql_query1 = """ CREATE TABLE users (
    uid integer PRIMARY KEY AUTOINCREMENT, 
    email text NOT NULL UNIQUE,
    uname text NOT NULL,
    name text NOT NULL,
    pswd text NOT NULL
)"""

sql_query2 = """ CREATE TABLE receipts (
    rid integer PRIMARY KEY AUTOINCREMENT, 
    total real NOT NULL,
    date text NOT NULL,
    category text NOT NULL,
    uid integer,
    FOREIGN KEY(uid) REFERENCES users(uid)
)"""
cursor.execute(sql_query1)
cursor.execute(sql_query2)
