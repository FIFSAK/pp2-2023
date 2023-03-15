import sqlite3 as sq

check = True
with sq.connect("PhoneBook.db") as con:
    cur = con.cursor()

    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        phone TEXT 
        )""")
    while check:
        print("[0] to exit\n[1] to add phone\n[2] to update phone\n[3] to delete phone\n[4] print data\n")
        n = int(input())
        if n == 0:
            check = False
        if n == 1:
            print("write name:")
            name = input()
            print("write phone:")
            phone = input()
            cur.execute("SELECT phone FROM users WHERE name = ? and phone = ?", (name, phone))
            if cur.fetchone() is None:
                cur.execute(f"INSERT INTO users VALUES (?, ?)", (name, phone))
            else:
                print("this entry already exists")
        if n == 2:
            print("write the user name which you want to update:")
            name = input()
            print("write the user phone which you want to update:")
            phone = input()
            print("write the new user name which you want to update:")
            new_name = input()
            print("write the new phone which you want to update:")
            new_phone = input()
            cur.execute("DELETE FROM users where name = ? and phone = ?", (name, phone))
            cur.execute(f"INSERT INTO users VALUES (?, ?)", (new_name, new_phone))

        if n == 3:
            print("write the user name which you want to delete:")
            name = input()
            print("write the user phone which you want to delete:")
            phone = input()
            cur.execute("DELETE FROM users where name = ? and phone = ?", (name, phone))
        if n == 4:
            for i in cur.execute("SELECT * FROM users"):
                print(i)
