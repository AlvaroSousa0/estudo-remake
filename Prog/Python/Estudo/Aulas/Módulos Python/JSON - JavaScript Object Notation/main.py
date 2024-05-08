import json
from dados import *


# dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# dicionario = json.loads(clientes_json)

# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)