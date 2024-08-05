class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._marca = None
        self._motor = None

    @property
    def fabricante(self):
        return self._marca


    @fabricante.setter
    def fabricante(self, nome):
        self._marca = nome
    

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        

    
class Motor:
    def __init__(self, nome):
        self.nome = nome
        


kicks = Carro('Kicks')
nissan = Fabricante('Nissan')
motor_3_0 = Motor('3.0')
kicks.fabricante = nissan
kicks.motor = motor_3_0
print(kicks.fabricante.nome, kicks.nome, kicks.motor.nome)



ram = Carro('RAM')
dodge = Fabricante('Dodge')
ram.fabricante = dodge
ram.motor = motor_3_0
print(ram.fabricante.nome, ram.nome, ram.motor.nome)
