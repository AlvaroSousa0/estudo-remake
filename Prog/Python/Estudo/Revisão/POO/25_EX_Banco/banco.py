import contas
import cliente


class Banco:
    def __init__(self, agencias:list[int] | None = None, contas:contas.Conta | None = None, clientes:cliente.Cliente | None = None):
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []
    

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('Agencia', True)
            return True
        else:
            return False
        

    def _Checa_conta(self, conta):
        if conta in self.contas:
            print('Conta', True)
            return True
        else:
            return False
        

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('Cliente', True)
            return True
        else:
            return False
        

    def _checa_se_conta_do_cliente(self, cliente, conta):
        if conta is cliente.contas:
            print('Cliente>conta', True)
            return True
        else:
            print('n pertence')
            return False
        

    def autenticar(self, cliente, conta):
        if self._checa_agencia(conta) and self._checa_cliente(cliente) and self._Checa_conta(conta) and self._checa_se_conta_do_cliente(cliente, conta):
           return True
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = cliente.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.contas = cc1
    c2 = cliente.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.contas = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.contas.depositar(100)
        print(c1.contas)