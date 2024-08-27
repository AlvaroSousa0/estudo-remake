# class ContextManager:
#     def __init__(self, caminho_arquivo, modo):
#         self.caminho_arquivo = caminho_arquivo
#         self.modo = modo
#         self._arquivo = None


#     def __enter__(self):
#         print('Abrindo o arquivo')
#         self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
#         return self._arquivo

#     def __exit__(self, class_exception_, exception_, traceback_,):
#         print('Fechando arquivo')
#         self._arquivo.close()

# with ContextManager('testingContextManager.txt', 'w') as ctxm:
#     ctxm.write('Linha 1 \n')
#     ctxm.write('Linha 2 \n')
#     print('With', ctxm)

from contextlib import contextmanager

@contextmanager
def myOpen(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()

with myOpen('testingContextManager.txt', 'a') as arquivo:
    arquivo.write('Linha1.2\n')
    arquivo.write('linha2.2\n')
    arquivo.write('linha3.2\n')
    print('With', arquivo)