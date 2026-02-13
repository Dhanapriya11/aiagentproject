from tools.db import get_connection

def get_schema():
    conn = get_connection()
    cursor = conn.cursor()

    schema = {}

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for (table,) in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        schema[table] = [col[1] for col in columns]

    conn.close()
    return schema
