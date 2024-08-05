class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def metodo_de_classe(cls):
        print('Método de classe..')

    @classmethod
    def criar_com_50(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anonimo', idade)
p1 = Pessoa('José', 31)

print(p1.nome)
print(Pessoa.ano)
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50('Helena')
p3 = Pessoa.criar_anonimo(30)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)