
# file = open('abc.txt','w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')

# file.seek(0, 2)
# print('Lendo linhas:')
# print(file.read())
# print('##############')

# file.seek(0,0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')

# file.seek(0,0)
# for linha in file.readlines():
#     print(linha, end='')


# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()



# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.write('Linha 4\n')
#     file.seek(0)
#     print(file.read())
#     file.close()

import json

d1 = {
    'Pessoa 1' : {
        'nome':'Luiz',
        'idade': 19
    },
    'Pessoa 2':{
        'nome':'Amy',
        'idade':20
    }
}
d1_json = json.dumps(d1, indent=True)

with open('abc.json','w+') as file:
    file.write(d1_json)
print(d1_json)
