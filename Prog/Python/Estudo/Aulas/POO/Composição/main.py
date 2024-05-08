from classes import Cliente

cliente1 = Cliente('Luiz', 35)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('Maria', 55)
print(cliente2.nome)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.lista_enderecos()
del cliente2
print()


cliente3 = Cliente('João', 20)
print(cliente3.nome)
cliente3.insere_endereco('São Paulo', 'SP')
cliente3.lista_enderecos()
del cliente3
print()


print('###########################################################################################')