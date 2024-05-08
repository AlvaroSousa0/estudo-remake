'''
Count - Itertools
'''
from itertools import count
# from types import GeneratorType

# variavel = ((x,y) for x, y in zip('Alo', 'Alo'))

# print(list(variavel))

contador = count(start= 5, step=0.2)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break