from dados import produtos, pessoas,lista

# def filtra(p):
#     if p['preço'] > 50:
#         return True

def maioridade(p):
    if p['idade'] > 18:
        return True

nova_lista = filter(maioridade, pessoas)
# nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))