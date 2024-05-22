import sqlite3
import function


print("Esse é o sistema de controle do Banco de Dados dos funcionários da empresa X.")
print(""" Ações disponíveis:
    'Adicionar', 'Visualizar', 'Remover' ou 'Modificar'""")
acao = input("Escolha a ação que deseja realizar: ").lower()
    


if acao == "adicionar":
    function.adicionar_funcionario()
    print()
elif acao == "modificar":
    function.modificar_funcionario()
    print()
elif acao == "remover":
    function.remover_funcionario()
    print()
elif acao == "visualizar":
    resultado = function.consultar_tabela()
    for valor in resultado:
        print(valor)
    print()
else:
        print("Essa função não existe!")
