import re
import random

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = remover_caracteres(cnpj)
    try:
        if teste_sequencia(cnpj):
            return False
    except:
        return False
    
    try:
        novo_cnpj = calcula_digito(cnpj=cnpj,digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj,digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regresivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regresivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None


    total = 0
    for indice,num in enumerate(regresivos):
        total += int(cnpj[indice]) * num
    
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def teste_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}00'
    novo_cnpj = calcula_digito(cnpj=inicio_cnpj,digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj,digito=2)
    return novo_cnpj

def formata(cnpj):
    cnpj = remover_caracteres(cnpj)
    formatado = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}.{cnpj[12:14]}'
    return formatado
