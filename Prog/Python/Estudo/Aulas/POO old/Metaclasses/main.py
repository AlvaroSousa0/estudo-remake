class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs,name,bases,namespace)        

        # if'b_fala' not in namespace:
        #     print(f'Oi, voce precisa criar o metodo b_fala em {name}')
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método.')

        if 'attr_classe' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']

        return type.__new__(mcs,name,bases,namespace)

class A(metaclass=Meta):
    attr_classe = 'Valor A'
    # def fala(self):
    #     self.b_fala()


class B(A):
    attr_classe = 'Valor B'
    # teste = 'Ai'

    # def b_fala(self):
    #     print('Oi')


    # def sla(self):
    #     pass


b = B()
print(b.attr_classe)

class Pai:
    nome = 'Teste'


Ab = type('Ab', (Pai,), {'attr':'Olá Mundo!'})

ab = Ab()
print(ab.nome)
