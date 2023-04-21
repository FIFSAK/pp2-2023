import sqlite3 as sq

user_name = input()
with sq.connect("snake_users_table.db") as con:
    cur = con.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        level NUM
        )""")

    cur.execute(f"SELECT name FROM users WHERE name = '{user_name}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?,?)", (user_name, '0'))
        level = 0
    else:
        cur.execute(f"SELECT level FROM users WHERE name = '{user_name}'")
        level = cur.fetchone()
        level = level[0]
    for i in cur.execute("SELECT * FROM users"):
        print(i)


def update(nm, nlv):
    with sq.connect("snake_users_table.db") as con:
        cur = con.cursor()
        cur.execute("UPDATE users SET level = ? WHERE name = ?", (nlv, nm))
