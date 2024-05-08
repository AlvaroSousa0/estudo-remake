def porcento(x, y):
    return x + (x * (y / 100))

conta = float(input('Digite o valor inteiro a ser aumentado. '))
porc = float(input('Digite a porcentagem para aumentar. '))
print(porcento(conta, porc))