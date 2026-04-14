import sqlite3
def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS employee
                   (
                       eid INTEGER PRIMARY KEY,
                       name TEXT,
                       email TEXT,
                       gender TEXT,
                       contact TEXT,
                       dob TEXT,
                       doj TEXT,
                       password TEXT,
                       utype TEXT,
                       adress TEXT,
                       salary TEXT
                   )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS supplier
                   (
                       invoice
                       INTEGER
                       PRIMARY
                       KEY,
                       name
                       TEXT,
                       contact
                       TEXT,
                       description
                       TEXT
                   )""")
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS category
                   (
                       cid
                       INTEGER
                       PRIMARY
                       KEY,
                       name
                       TEXT
                   )""")
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS product
                   (
                       pid
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       category
                       TEXT,
                       supplier
                       TEXT,
                       name
                       TEXT,
                       product
                       TEXT,
                       price
                       TEXT,
                       qty
                       TEXT,
                       status
                       TEXT
                   )""")
    con.commit()


    con.close()

create_db()