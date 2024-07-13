class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    
class Professor(Pessoa):
    def falar(self):
        print('Classe professor')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    def falar(self):
        print('Classe aluno')
        print(self.nome, self.sobrenome, self.__class__.__name__)


p1 = Professor('Everaldo', 'Costa')
a1 = Aluno('Antonio', 'José')
p1.falar()
a1.falar()