import os
from utils import formata


caminho = input('Digite um Caminho ')
termo_busca = input('Digite um termo ')


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo_busca in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo.')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {ext_arquivo}')
                print(f'Tamanho: {tamanho}')
                print(f'Tamanho formatado {formata(tamanho)}')
                print(f'{conta} arquivo(s) encontrado(s).')
            except PermissionError as e:
                print('Sem permissão neste arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido', e)