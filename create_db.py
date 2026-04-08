import sqlite3
def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS employee(
        eid INTEGER PRIMARY KEY,
        name text,
        email text,
        gender text,
        contact text,
        dob text,
        doj text,
        pass text,
        utype text,
        adress text,
        salary text,
    )""")
    con.commit()

create_db()