import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


if __name__ == '__main__':
    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    " name TEXT,"
    " weight REAL"
    ")"
    )
    con.commit()


    # cursor.execute(f'INSERT INTO {TABLE_NAME}(id, name, weight) VALUES (NULL, "Pedro", 12)')
    # con.commit()

    # cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id>"5"')
    # con.commit()


    cursor.execute(f'UPDATE {TABLE_NAME} '
                   'SET weight="100" '
                   'WHERE id=20')
    con.commit()

    
    # sql = (f'INSERT INTO {TABLE_NAME}(name, weight) VALUES (:nome, :peso)')
    # cursor.execute(sql, ['Carlos', 32])
    # con.commit()
    # print(sql)

    # cursor.executemany(sql, [
    #     {'nome':'Paulo', 'peso': 9},
    #     {'nome':'Flávio', 'peso': 1},
    #     {'nome':'Gian', 'peso':7}
    #     ])
    # con.commit()



    cursor.close()
    con.close()