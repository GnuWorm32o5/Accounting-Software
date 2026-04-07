import sqlite3
def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS employee(
        eid INTEGER PRIMARY KEY AUTOINCREMENT,
        dz text,
        di text,
        name text,
        lname text,
        contact text,
        user text,
        pass text,
        email text,
        adress text,
        pay text,
        usertype text
    )""")
    con.commit()

create_db()