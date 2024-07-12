# Associação
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None


    @property
    def ferramentaF(self):
        return self._ferramenta
    

    @ferramentaF.setter
    def ferramentaF(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome


    def escrever(self):
        return f'{self.nome} está escrevendo'
    

# escritor = Escritor('José')
# ferramentaVar = FerramentaDeEscrever('Caneta Bic')
# escritor.ferramentaF = ferramentaVar
# print(escritor.ferramentaF.escrever())


# Associação

##################################################################################################

# Agregação


class Carrinho:
    def __init__(self) -> None:
        self._produtos = []

    def total(self):
        return sum(self._produtos)
        

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)