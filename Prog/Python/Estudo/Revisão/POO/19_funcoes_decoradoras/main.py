def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Voce está em casa.'
        return resultado
    return interno


# @add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


# @add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


# time1 = Time('Vasco')
# time2 = Time('Fluminense')

planeta = Planeta('Terra')
planeta2 = Planeta('Venus')

# print(time1)
# print(time2)
# print()
print(planeta.falar_nome())
print(planeta2.falar_nome())