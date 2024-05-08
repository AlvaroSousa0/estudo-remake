palavra_secreta = 'garrafa'
digitadas = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta.')
        digitadas.pop()

    secreto_temp = ''
    for letras in palavra_secreta:
        if letras in digitadas:
            secreto_temp += letras
        else: 
            secreto_temp += '*'
    
    if secreto_temp == palavra_secreta:
        print(f'Você venceu, a palavra era "{palavra_secreta}"')
        break
    else:
        print(f'A palavra secreta está assim "{secreto_temp}"')
        
    