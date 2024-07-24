from abc import ABC, abstractmethod


# class Log(ABC):
#     @abstractmethod
#     def _log(self, msg): ...    

#     def log_error(self, msg):
#         return self._log(f'Error: {msg}')
    

#     def log_success(self, msg):
#         return self._log(f'Success: {msg}')


# class LogFileMixin(Log):
#     def _log(self, msg):
#         msg_formatada = f'{msg} ({__class__.__name__})'
#         return msg_formatada

# class LogPrintMixin(Log):
#     def _log(self, msg):
#         msg_formatada = f'{msg} ({__class__.__name__})'
#         return msg_formatada   

# l = LogPrintMixin()
# print(l.log_error('OI'))




class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

        @property
        @abstractmethod
        def name(self): ...

     
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name