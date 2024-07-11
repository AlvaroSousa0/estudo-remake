# @property é um método que se comporta como atributo


class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
    

caneta = Caneta('Azul')
caneta.cor = 'verde'
print(caneta.cor)
