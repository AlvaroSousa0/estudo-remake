ano_atual = 1
class Pessoa:

    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100

    def ano_nascimento(self):
        print(f'{Pessoa.ano_atual - self.idade}\n')
    
p1 = Pessoa('José', 43 )
p2 = Pessoa('Alline', 25 )

# p1.ano_nascimento()
# p2.ano_nascimento()

p1.nome = 'Carlos'
p1.__dict__['nome'] = 'Kirito'
print(p1.__dict__)
print(vars(p1))