from main import Pessoa, CAMINHO_ARQUIVO
import json

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoa = json.load(arquivo)


    p1 = Pessoa(**pessoa[0])
    p2 = Pessoa(**pessoa[1])

    print(p1.nome)
    print(p2.idade)