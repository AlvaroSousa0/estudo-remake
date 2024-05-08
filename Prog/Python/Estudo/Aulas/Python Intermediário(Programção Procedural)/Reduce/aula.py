from dados import produtos,pessoas,lista
from functools import reduce

acumula = 0

# for item in lista:
#     acumula += item
# print(acumula)

# soma_lista = reduce(lambda ac,i: i + ac,lista,0)
soma_precos = reduce(lambda ac, p: p['preço'] + ac, produtos,0)
print(soma_precos)