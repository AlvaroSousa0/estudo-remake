from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo


    def depositar(self, valor):
        if isinstance(valor,(int, float)):
            self.saldo += valor
            self.detalhes()


    @abstractmethod
    def sacar(self, valor):
        pass


    def detalhes(self):
        print(f'Agência: {self.agencia} ')
        print(f'Conta: {self.conta} ')
        print(f'Saldo: {self.saldo} ')


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)


    def sacar(self, valor):
        if isinstance(valor,(int, float)):
            if valor < self.saldo:
                self.saldo -= valor
                self.detalhes()
                return
            else:
                print('Saldo insuficiente. ')
                return
        else:
            print('valor precisa ser numérico.')
            return


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    
    def sacar(self, valor):
        if isinstance(valor,(int, float)):
            if valor < (self.saldo + self.limite):
                self.saldo -= valor
                self.detalhes()
                return
            else:
                print('Saldo insuficiente. ')
                return
        else:
            print('valor precisa ser numérico.')
            return