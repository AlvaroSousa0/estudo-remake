class Banco:
    def __init__(self):
        self.agencias = [1050, 5750, 6520]
        self.clientes = []
        self.contas = []


    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)


    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if not cliente in self.clientes and cliente.conta in self.contas and cliente.conta.agencia in self.agenciass:
            print('Você não é cliente do nosso banco.')
            return False
        return True