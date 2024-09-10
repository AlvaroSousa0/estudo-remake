def meu_repr(self):
    return f'{type(self).__name__}({self.__dict__})'
class Meta(type):
    def __new__(mcs, name, bases, dict):
        print('META NEW')
        cls = super().__new__(mcs, name, bases, dict)
        cls.attr = 1234
        cls.__repr__ = meu_repr


        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Implemente falar')


        return cls
    
    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError('Crie o attr nome')
        return instancia



class Pessoa(metaclass= Meta):
    def __new__(cls, *args, **kwargs):
        print('meu new')
        instancia = super().__new__(cls)
        return instancia
    

    def __init__(self, nome):
        print('Meu init')
        self.nome = nome

    def falar():
        print('falando')


p1 = Pessoa('Luiz')
print(p1)
