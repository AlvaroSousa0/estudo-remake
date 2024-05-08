
# def fala_oi():
#     print('Oi')

# var = fala_oi
# print(type(var))

def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)

outra_funcao('Ola, eu sou o doutor.')


# fala_oi = master(fala_oi)
# fala_oi()
