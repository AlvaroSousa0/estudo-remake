from main import DB_FILE, TABLE_NAME
import sqlite3
from pathlib import Path


con = sqlite3.Connection(DB_FILE)
cursor = con.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

for row in cursor.fetchall():
    print(row)
    _id, nome, peso = row
    # print(_id, nome, peso)

cursor.close()
con.close()