import banco
import contas
import cliente


"""
Exercício sistema de banco básico

Minha visão - não me sai bem .
Preciso melhorar lógica e entendimento do desafio
praticamente inteiro copiado.

"""

c1 = cliente.Cliente('José', 23)
cc1 = contas.ContaCorrente(111, 2345, 234, 20)
c1.contas = cc1


c2 = cliente.Cliente('Pedro', 43)
cp1 = contas.ContaPoupanca(222, 1029, 2300000)
c2.contas = cp1

c1.contas.depositar(2)
c1.contas.sacar(2300002)

banco = banco.Banco()
banco.clientes.extend([c1, c2])
banco.contas.extend([cc1, cp1])
banco.agencias.extend([111,222])


if banco.autenticar(c1, cc1):
    c1.contas.depositar(1234)
    c1.contas.sacar(1488)
    
