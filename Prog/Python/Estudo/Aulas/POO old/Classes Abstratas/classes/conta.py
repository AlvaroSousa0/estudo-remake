from abc import ABC, abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo


    def depositar(self, valor):
        if not isinstance(valor,(int,float)):
            raise ValueError('Saldo precisa ser numérico.')

        self.saldo += valor
        self.detalhes()


    def detalhes(self):
        print(f'Agência: {self.agencia} ')
        print(f'Conta: {self.conta} ')
        print(f'Saldo: {self.saldo} ')


    @abstractmethod
    def sacar(self, valor):
        pass