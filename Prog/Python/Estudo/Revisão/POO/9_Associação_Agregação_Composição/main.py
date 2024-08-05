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
        return sum(p.preco for p in self._produtos)
        

    def adicionar_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


# carrinho = Carrinho()
# p1, p2 = Produto('Caneta', 1.50), Produto('Cadeira', 192.35)
# carrinho.adicionar_produtos(p1, p2)
# carrinho.listar_produtos()
# print(carrinho.total())


#Agregação

##################################################################################################

#Composição


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    
    def inserir_endereços(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))


    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero





c1 = Cliente('Amara')
c1.inserir_endereços('José Fagundes', 192)
c1.inserir_endereços('Avenida Brasil', 4023)
c1.listar_enderecos()


#Composição