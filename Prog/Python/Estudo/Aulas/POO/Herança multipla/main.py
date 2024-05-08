# class A:
#     def falar(self):
#         print('Falando.. Estou em A')


# class B(A):
#     def falar(self):
#         print('Falando... estou em B')


# class C(A):
#     def falar(self):
#         print('Falando... estou em C')


# class D(C, B):
#     pass


# d = D()
# d.falar()




from smartphone import Smartphone


smartphone = Smartphone('PocoPhone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.ligar()
smartphone.desconectar()
smartphone.conectar()
smartphone.desconectar()