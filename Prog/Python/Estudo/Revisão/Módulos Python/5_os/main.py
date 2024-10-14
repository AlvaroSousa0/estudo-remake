import os 


# os.system('clear')
# os.system('echo "Hello world"')


# # print('a'*800)

# caminho = os.path.join('/home', 'alvaro', 'Documentos', 'GitHub', 'estudo-remake', 'Prog', 'Python', 'main.py')
# # print(caminho)
# diretorio, arquivo = os.path.split(caminho)
# # print(diretorio)
# # print(arquivo)
# nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
# # print(nome_arquivo, extensao_arquivo)
# print(os.path.exists(caminho))
caminho = os.path.join('/home', 'alvaro', 'Imagens')

for item in os.listdir(caminho):
    
    caminho_completo = os.path.join(caminho, item)
    print(item)

    for imagem in os.listdir(caminho_completo):
        print(' ', imagem)