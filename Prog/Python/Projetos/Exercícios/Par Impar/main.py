while True:
    num = input('Digite um número inteiro: ')

    try:
        num = int(num)
        if num % 2 == 0:
            print('O número digitado é par.')
        else:
            print('O número digitado é impar.')
    except ValueError:
        print('Digite um número inteiro.')
