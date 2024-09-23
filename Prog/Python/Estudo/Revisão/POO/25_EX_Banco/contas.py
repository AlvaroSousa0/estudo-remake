import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int,conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> None:...


    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.aviso(f'Você depositou {valor}, saldo atual:')


    def aviso(self,msg: str) -> None:
        print(f'{msg} R${self.saldo}')


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> None:
        if self.saldo >= valor:
            self.saldo -= valor
            self.aviso(f'Você sacou R${valor}, saldo restante:')
        else:
            self.aviso('Saldo insuficiente')


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float, limite: float):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor: float) -> None:
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

    