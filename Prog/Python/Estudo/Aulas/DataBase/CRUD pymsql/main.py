import pymysql.cursors
from contextlib import contextmanager
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host ='127.0.0.1',
        user='root',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' 
        '(%s, %s, %s, %s)'
        dados = [
            ('Jack', 'Monroe', 112, 100), ('Kiyu', 'Jones', 795, 22),
            ('John', 'Maverick', 70, 3000), ('Gorlock', 'The Destroyer', 203, 534)
        ]
        cursor.executemany(sql, dados)
        cursor.commit()

with conecta() as conexao:        
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()
        
        for linha in resultado:
            print(linha)
