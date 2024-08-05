# class Pessoa:
#     def __init__(self, nome, sobrenome):
#         self.nome = nome
#         self.sobrenome = sobrenome

    
# class Professor(Pessoa):
#     def falar(self):
#         print('Classe professor')
#         print(self.nome, self.sobrenome, self.__class__.__name__)


# class Aluno(Pessoa):
#     def falar(self):
#         print('Classe aluno')
#         print(self.nome, self.sobrenome, self.__class__.__name__)


# p1 = Professor('Everaldo', 'Costa')
# a1 = Aluno('Antonio', 'José')
# p1.falar()
# a1.falar()

#############################################################################################################

# class MinhaString(str):

#     def upper(self):
#         print('antes do super')
#         retorno = super().upper()
#         print('depois do super')
#         return retorno + ' POCOTÓ'
    

# string = MinhaString('upaupa')
# print(string)
# print(string.upper())

class A:
    atributo_a = 'Valor A'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'Valor B'

    def metodo(self):
        print('B')

    
class C(B):
    atributo_c = 'Valor C'

    def metodo(self):
        super(B, self).metodo()
        super().metodo()
        print('C')
        

c = C()
print(c.atributo_a)
print(c.atributo_b) 
print(c.atributo_c)        
c.metodo()