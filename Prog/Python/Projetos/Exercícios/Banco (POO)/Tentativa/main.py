from classes.banco import Banco
from classes.cliente import Cliente
from classes.conta import ContaPoupanca, ContaCorrente


banco = Banco()
c1 = Cliente('Jose', 34)
c2 = Cliente('Pedro', 23)
c3 = Cliente('Beatriz', 22)


conta1 = ContaPoupanca(1111, 123456, 0)
conta2 = ContaPoupanca(2222, 234567, 0)
conta3 = ContaCorrente(5555, 124589,0)


banco.inserir_clientes(c1)
banco.inserir_conta(conta1)

c1.inserir_conta(conta1)
c2.inserir_conta(conta2)
c3.inserir_conta(conta3)

if banco.autenticar(c1):
    c1.conta.depositar(150)
    print()
    c1.conta.sacar(30)
else:
    print('Cliente não autenticado.')