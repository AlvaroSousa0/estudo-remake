import re

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
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None


    total = 0
    for indice,num in enumerate(regressivos):
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
