"""
Documentação de funções

"""
var_1 = 1
def soma(x:int|float,y:int|float) -> int|float:
    """
    Soma x e y

    :param x: numero 1
    :type x: int or float
    :param y: numero 2
    :type y: int or float


    :return: A soma de x e y
    :rtype: int or float
    """
    return x + y


def multiplica(x:int|float, y:int|float,z:int|float|None = None) -> int|float:
    if z is None:
        return x * y
    return x * y * z