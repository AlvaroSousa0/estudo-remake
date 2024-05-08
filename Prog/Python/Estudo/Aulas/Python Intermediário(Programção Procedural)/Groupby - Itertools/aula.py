from itertools import groupby, tee
alunos = [
    {'nome':'Molusco','nota':'F'},
    {'nome':'Jonisvaldo','nota':'C'},
    {'nome':'Raymond Holt','nota':'A'},
    {'nome':'Portulo','nota':'B'},
    {'nome':'Saussarina','nota':'C'},
    {'nome':'Milson','nota':'A'},
    {'nome':'Etchevery','nota':'A'}
]
ordena = lambda item: item['nota']

alunos.sort(key=ordena)

alunos_aguprado = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_aguprado:
    va1 , va2= tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade}')
    print()