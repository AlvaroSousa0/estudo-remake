# Mutáveis --> Listas, Dicionários
# Imutáveis --> Tuplas, Strings, Números, True, False, None

# def lista_de_clientes(clientes_iteravel, lista=[]):
#     lista.extend(clientes_iteravel)
#     return lista

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista == None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
print(clientes1)
print(clientes2)