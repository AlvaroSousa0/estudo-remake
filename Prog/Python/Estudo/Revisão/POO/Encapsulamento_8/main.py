class Foo:
    def __init__(self):
        self.public = 'Isso é público'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso é privado'

    def metodo_publico(self):
        return 'Método publico'
    

    def _metodo_protected(self):
        return 'Metodo Protegido'
    

    def __metodo_privado(self):
        return 'Método Privado'


f = Foo()
print(f.public)
print(f.metodo_publico())
print(f._protected)
print(f._metodo_protected())
print(f.__private)
print(f.__metodo_privado())