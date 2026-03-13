import sqlite3

db = sqlite3.connect("database.db")
cur = db.cursor()

cur.execute("""
CREATE TABLE users(
    name TEXT,
    email TEXT,
    password TEXT
)
""")

db.commit()
db.close()
