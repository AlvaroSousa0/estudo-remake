while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')

    if not num_1.isalpha() and not num_2.isalpha():
        try:
            num_1 = int(num_1)
        except:
            num_1 = float(num_1)
        
        try:
            num_2 = int(num_2)
        except:
            num_2 = float(num_2)

        operacao = input('Escolha a operação a ser feita. Ex. +, -, *, / : ')
        resultado = None

        if operacao == '+':
            resultado = num_1 + num_2
            print(resultado)
        elif operacao == '-':
            resultado = num_1 - num_2
            print(resultado)
        elif operacao == '*':
            resultado = num_1 * num_2
            print(resultado)
        elif operacao == '/':
            resultado = num_1 / num_2
            print(resultado)

    else:
        print('Digite apenas números. ')