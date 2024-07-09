class Carro:
    def __init__(self, nome, ligado=False):
        self.nome = nome 
        self.ligado = ligado

    def ligar(self):
        if self.ligado:
            print(f'{self.nome} já está ligado')
        else:
            print(f'{self.nome} foi ligado.')
            self.ligado = True

    def desligar(self):
        if self.ligado == False:
            print(f'{self.nome} já está desligado')
        else:
            print(f'{self.nome} foi desligado.')
            self.ligado = False


civic = Carro('Civic')
civic.desligar()
civic.ligar()
civic.ligar()