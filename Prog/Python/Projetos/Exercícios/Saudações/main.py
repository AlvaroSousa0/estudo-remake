while True:

    horario = input('Olá, que horas são? ')

    try:
        horario = int(horario)

        if horario >= 0 and horario <= 11:
            print('Bom Dia!!')
        elif horario >= 12 and horario <= 17:
            print('Boa Tarde!!')
        elif horario >= 18 and horario <= 23:
            print('Boa Noite!!')
        elif horario > 23:
            print('Digite um horário até 23 horas.')
    except ValueError:
        print('Digite o horário em número inteiro e sem pontuação.')
    