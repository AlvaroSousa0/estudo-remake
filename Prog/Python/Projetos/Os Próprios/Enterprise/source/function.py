import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho_db = '/home/alvaro/GitHub/Prog-E/Prog/Python/Projetos/Os Próprios/Enterpise/db/funcionarios.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho_db)
    except Error as er:
        print(er)
    return conexao

conexao = conexaoBanco()


def adicionar_funcionario():
    nome = input('\nNome completo do funcionário: ')
    contato = input('Número de telefone ou email para contato: ')
    cargo = input('Cargo do funcionário: ')
    turno = input('Turno do funcionário: ')
    escolaridade = input('Escolaridade do funcionário: ')
    nivel_con = input('Nível de conhecimento do funcionário na área designada: ')

    sql = f"""INSERT INTO funcionarios(nome, contato, cargo, turno, escolaridade, nivelConhecimento)
      VALUES ('{nome}', '{contato}', '{cargo}', '{turno}', '{escolaridade}', '{nivel_con}')"""
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print('Funcionário adicionado.\n')


def remover_funcionario():
    identificador = input("\nDigite o 'id' do funcionário: ")
    if len(identificador) > 0:
        sql = f"DELETE FROM funcionarios WHERE id_funcionario='{identificador}'"
    else:
        nome = input('\nDigite o nome do funcionário: ')
        contato = input('Digite o contato do funcionário: ')
        sql = f"DELETE FROM funcionarios WHERE nome='{nome}' and contato='{contato}'"
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)


def modificar_funcionario():
    identificador = input("\nDigite o 'id' do funcionário que deseja modificar: ")
    modifica = input('Digite um item que deseja modificar: ')
    novo_valor = input('Digite o que deseja colocar: ')
    sql = f"UPDATE funcionarios SET '{modifica}'='{novo_valor}' WHERE id_funcionario='{identificador}'"
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print('Modificado com sucesso.\n')
    

def consultar_tabela():
    cargo_filtro = input('\nDigite o cargo pelo qual deseja filtrar: ')
    sql = f"SELECT * FROM funcionarios WHERE cargo='{cargo_filtro}'"
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        return resultado
    except Error as er:
        print(er)
    