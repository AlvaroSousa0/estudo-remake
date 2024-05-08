from itertools import zip_longest, count

'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''

### Código
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Fortaleza','Buenos Aires']

### Código

estados = ['SP', 'MG', 'BA', 'CE']

cidades_estados = zip(indice,estados,cidades)
for indice,estados,cidades in cidades_estados:
    print(indice,estados,cidades)
# for v in cidades_estados:
#     print(v)