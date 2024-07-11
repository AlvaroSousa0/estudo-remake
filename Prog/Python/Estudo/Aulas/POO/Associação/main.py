from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joel')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(caneta.marca)
print(escritor.nome)
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# del escritor
print(escritor)
maquina.escrever()