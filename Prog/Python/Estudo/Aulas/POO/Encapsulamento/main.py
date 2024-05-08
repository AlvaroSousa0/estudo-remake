'''
public, protected, private
_ Privado/protected (public com _)(não mexa!!)
__ Privado(_NomeClasse__NomeAtributo)(Não mexa em hipotese alguma!!!!)
'''

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})


    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'João')
bd.inserir_cliente(2, 'Batista')
bd.__dados = 'Outra coisa'
bd.lista_clientes()
# print(bd.__dados)
# print(bd._BaseDeDados__dados)
print(bd.dados)