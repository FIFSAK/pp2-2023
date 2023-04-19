import sqlite3 as sq
import psycopg2

user_name = input()
with psycopg2.connect(dbname="postgres", user="postgres", password=" ", host="127.0.0.1") as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        level int
        )""")

    cur.execute(f"SELECT name FROM users WHERE name = '{user_name}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES ('{user_name}',0)")
        level = 0
    else:
        cur.execute(f"SELECT level FROM users WHERE name = '{user_name}'")
        level = cur.fetchone()
        level = level[0]
    cur.execute("select * from users")
    data = cur.fetchall()
    for i in data:
        print(i)


def update(nm, nlv):
    with psycopg2.connect(dbname="postgres", user="postgres", password=" ", host="127.0.0.1") as con:
        cur = con.cursor()
        cur.execute(f"UPDATE users SET level = '{nlv}' WHERE name = '{nm}'")
