a = {}

try:
    print(a)
except NameError as erro:
    print('Erro do dev,fale com ele')
except (IndexError, KeyError) as erro:
    print('Erro de índice')
except Exception as erro:
    print('Erro desconhecido.')
else:
    # print('Seu bloco foi executado com sucesso.')
    pass
finally:
    # print('Finalmente')
    pass
print('continuando')