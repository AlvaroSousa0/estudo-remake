# from collections import namedtuple

# Carta = namedtuple('Carta', ['Valor', 'Naipe'], defaults=['VALOR', 'NAIPE'])




from typing import NamedTuple

class Carta(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'

as_espadas = Carta('A', 'Espadas')
um_espadas = Carta('1', 'Espadas')


print(as_espadas._asdict())
print(as_espadas[0])
print(as_espadas[1])

print(as_espadas._field_defaults)
print(as_espadas._fields)