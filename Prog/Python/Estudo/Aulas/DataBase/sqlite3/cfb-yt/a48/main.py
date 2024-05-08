import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = '/home/alvaro/GitHub/Prog-E/Prog/Python/Estudo/Aulas/DataBase/sqlite3/cfb-yt/db/agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con

vcon = conexaoBanco()

vsql = """CREATE TABLE tb_contatos(
N_idContato INTEGER PRIMARY KEY AUTOINCREMENT,
T_nomeContato VARCHAR(30),
T_telefoneContato VARCHAR(14),
T_emailContato VARCHAR(30)
);"""

def criarTabela(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as er:
        print(er)
        
# criarTabela(vcon,vsql)


vcon.close()