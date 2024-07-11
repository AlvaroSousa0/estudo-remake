from dataclasses import dataclass



@dataclass(eq=True, repr=True, order=False, frozen=False, init=True)
class Pessoa:
    nome:str
    sobrenome:str


    def __post_init__(self):
        if not isinstance(self.nome,str):
            raise TypeError(f'Tipo inválido {type(self.nome)} != str em {self}')

    @property
    def nome_completo(self):
         return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('A', '5')
# p2 = Pessoa(2345, '3')
p3 = Pessoa('C', '4')
p4 = Pessoa('B', '7')

pessoas = [p1,p3,p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))

print(p1.nome_completo)