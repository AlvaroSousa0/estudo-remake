class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa("João", "Neto")
# print(p1.nome)
# print(p1.sobrenome)



class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando.')

    def freiar(self):
        print(f'{self.nome} está freiando.')
    
    def parar(self):
        print(f'{self.nome} parou.')
audi = Carro("Audi")
audi.acelerar()
Carro.acelerar(audi)
audi.freiar()
Carro.parar(audi)