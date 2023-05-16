import sqlite3

conn = sqlite3.connect("quit.db")
cursor = conn.cursor()
cursor.execute('''  INSERT INTO USER (
    USERNAME, PASSWORD) VALUES("a",  "a")''')
conn.commit()
print("Records inserted........")

# Closing the connection
conn.close()