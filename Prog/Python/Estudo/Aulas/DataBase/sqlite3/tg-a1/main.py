import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
# 'id INTEGER PRIMARY KEY AUTOINCREMENT,'
# 'nome TEXT,'
# 'peso REAL'
# ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Ronald Conan", 80.5)')
# conexao.commit()
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)',
#  ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#  ({'nome':'José', 'peso':'65'}))
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#  ({'id': None,'nome':'Beto', 'peso':'110'}))
# conexao.commit() 

# cursor.execute('DELETE FROM clientes where id=:id',{'id': 2})
# conexao.commit()


cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

for linha in cursor.fetchall():
    nome, peso = linha

    print(nome, peso)
    


cursor.close()
conexao.close()
