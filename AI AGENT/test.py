import sqlite3

conn = sqlite3.connect("dataset/Chinook_Sqlite.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.close()
