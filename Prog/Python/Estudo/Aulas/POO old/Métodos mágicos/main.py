class A:
    def __init__(self):
        pass

    
    # def __new__(cls,*args,**kwargs):
        
    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)

    #     return cls._jaexiste


    # def __call__(self, *args, **kwargs):
    #     resultado = 1

    #     for i in args:
    #         resultado *= i 
    #     return resultado


    # def __setattr__(self, key,value):
    #     if key == 'nome':
    #         self.__dict__[key] = 'Você não pode fazer isso'
    #     else:
    #         self.__dict__[key] = value


    # def __del__(self):
    #     print('Objeto Coletado')


    # def __str__(self):
    #     return 'Essa é a clase A criada para alguma coisa'


    # def __len__(self):
    #     return 55


a = A()
print(len(a))