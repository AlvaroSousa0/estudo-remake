class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        return self.func(*args, **kwargs) * self._multiplicador



    
@Multiplicar
def soma(x, y):
    return x+y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)