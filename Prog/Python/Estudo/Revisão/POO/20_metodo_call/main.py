class CallMe:
    def __init__(self,phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Está chamando', self.phone)
call1 = CallMe('1234423432323')
call1('João')



class Carro:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    def __call__(self):
        print(f'Seu carro é {self.nome} com uma potência de {self.potencia} cavalos')


porsche = Carro('Porsche Cayenne', 700)
porsche()