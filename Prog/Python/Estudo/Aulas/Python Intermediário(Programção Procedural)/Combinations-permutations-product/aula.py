'''
Combinations, Permutations, Product - Itertools
Combinação - ordem não importa
Permutação - ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
'''
from itertools import combinations,permutations,product

pessoas = ['João', 'José', 'Maria', 'André', 'Rufus', 'Holt', 'Raymond']

for grupo in permutations(pessoas,2):
    print(grupo)
for grupo in product(pessoas,repeat=2):
    print(grupo)
for grupo in combinations(pessoas, 2):
    print(grupo)
