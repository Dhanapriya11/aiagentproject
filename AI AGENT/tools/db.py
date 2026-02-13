import sqlite3

DB_PATH = "dataset/Chinook_Sqlite.sqlite"

def get_connection():
    return sqlite3.connect(DB_PATH)
