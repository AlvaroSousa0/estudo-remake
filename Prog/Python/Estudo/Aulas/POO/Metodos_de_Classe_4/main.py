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


p1 = Pessoa('José', 31)

print(p1.nome)
print(Pessoa.ano)
Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50('Helena')
print(p2.nome, p2.idade)