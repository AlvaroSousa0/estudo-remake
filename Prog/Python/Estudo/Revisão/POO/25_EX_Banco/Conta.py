from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia:int, conta:int, saldo:int|float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor:int|float) -> None:...

    def depositar(self, valor:int|float) -> None:
        self.saldo += valor
        self.aviso(f'Você depositou {valor}, saldo atual:')


    def aviso(self,msg:str) -> None:
        print(f'{msg} R${self.saldo}')


class ContaPoupanca(Conta):
    def sacar(self, valor:int|float) -> None:
        if self.saldo >= valor:
            self.saldo -= valor
            self.aviso(f'Você sacou R${valor}, saldo restante:')
        else:
            self.aviso('Saldo insuficiente')


class ContaCorrente(Conta):
    def sacar(self, valor:int|float) -> None:
        self.limite = 150
        if valor > self.saldo and valor <= self.saldo+self.limite:
            self.diferenca = valor - self.saldo
            self.limite -= self.diferenca
            self.diferenca = 0
            self.saldo -= valor
            self.aviso(f'Você sacou {valor} usando o limite, saldo:')

        elif valor <= self.saldo:
            self.saldo -= valor
            self.aviso(f'Você sacou {valor}, saldo restante:')
        else:
            print('valor indisponível para saque.')
            print(f'Valor máximo disponível de saque {self.saldo + self.limite}')
