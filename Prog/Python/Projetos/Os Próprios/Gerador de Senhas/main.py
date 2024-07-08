import random, string

while True:
    qtd_caracteres = int(input('Quantos caracteres deve ter a senha? '))

    senha = ''

    while len(senha) < qtd_caracteres:
        letra_numero_ou_especial = random.randint(0,2)
        if letra_numero_ou_especial == 0:
            senha += random.choice(string.ascii_letters)
        elif letra_numero_ou_especial == 1:
            caracteres_especiais = '!@#$%&*-+=~^?/:;.,<>'
            escolha_caractere = random.randint(0,19)
            senha += caracteres_especiais[escolha_caractere]
        else: 
            senha += str(random.randint(0,9))

    print(senha)