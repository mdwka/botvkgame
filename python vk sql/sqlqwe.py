import sqlite3
conn = sqlite3.connect(r'/Users/ivanzvagin/Desktop/sqltest.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS messages(
    msg_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
    msgtxt TEXT);
""")
conn.commit()

def sender(sql):
     cur.execute("INSERT INTO messages(msgtxt) VALUES('{}');".format(sql))
     conn.commit()