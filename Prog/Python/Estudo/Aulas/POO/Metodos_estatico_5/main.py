class Estatico:
    @staticmethod
    def funcao_estatica(*args, **kwargs):
        print(args, kwargs)

    


c1 = Estatico.funcao_estatica('olá POO', Panda='O Dragão Guerreiro')
Estatico.funcao_estatica('Skadush', 'hahahahahah', Skadush='Ataque mortal')