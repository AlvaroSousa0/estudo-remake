import enum 

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


def mover(direcoes):
    if not isinstance(direcoes, Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcoes.name}({direcoes.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.ACIMA)
mover(Direcoes.DIREITA)
mover(Direcoes.ABAIXO)

# mover('lado')