from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self,nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado.'
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f'{self._nome} ja está conectado.'
            print(error)
            self.log_error(error)
            return


        info = f'{self._nome} está conectado.'
        print(info)
        self.log_info(info)
        self._ligado = True


    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            self._conectado = True
            return

        info = f'{self._nome} foi desconectado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False