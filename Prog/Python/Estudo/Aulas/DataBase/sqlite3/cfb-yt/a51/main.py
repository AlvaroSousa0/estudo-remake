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

# nome = input('Digite o nome ')
# telefone = input('Digite o telefone ')
# email = input('Digite o email ')

# vsql = f"""insert into tb_contatos(T_nomeContato,T_telefoneContato,T_emailContato) values
# ('{nome}','{telefone}','{email}')
# """

def inserir(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print("Registro inserido")

# inserir(vcon,vsql)

def deletar(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print("Registro deletado")


# vsql = "delete from tb_contatos where N_idContato=4"
# deletar(vcon,vsql)


def update(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()    
    except Error as er:
        print(er)
    finally:
        print("Registro Atualizado")


vsql = "UPDATE tb_contatos SET T_nomeContato='Roberto Carlos', T_telefoneContato = '45 99345 9232', T_emailContato='novodia@novotempo.com' WHERE N_idContato=1"

update(vcon,vsql)