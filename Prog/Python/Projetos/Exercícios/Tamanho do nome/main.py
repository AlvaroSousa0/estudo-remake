while True:

    nome = input('Qual é o seu primeiro nome? ')

    if len(nome) <= 4:
        print('Seu nome é curto. ')
    elif len(nome) > 4 and len(nome) <= 6:
        print('Seu nome é normal. ')
    elif len(nome) > 6:
        print('Seu nome é grande. ')
