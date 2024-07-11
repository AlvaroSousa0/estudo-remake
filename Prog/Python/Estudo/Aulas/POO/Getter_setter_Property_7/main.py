# @property é um método que se comporta como atributo


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Coisas')
        return self.cor_tinta

caneta = Caneta('Azul')

print(caneta.cor)