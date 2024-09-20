class Banco:
    AGENCIAS = [1,23,65,89,124]
    CLIENTES = []

    def autenticar_clientes(self, cliente):
        self.cliente = cliente
        if self.cliente.numero_conta in Banco.CLIENTES:
            print('a')
            return True
        else:
            print('b')
            return False


