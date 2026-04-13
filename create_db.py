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
                       invoiceINTEGER PRIMARY KEY,
                       name TEXT,
                       contact TEXT,
                       description TEXT
                   )""")
    con.commit()
    con.close()

create_db()