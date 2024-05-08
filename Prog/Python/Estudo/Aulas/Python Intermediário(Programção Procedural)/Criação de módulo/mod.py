import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i 
    return r
if __name__ == '__main__':
    list = [1,2,3,4,5,6]
    print(dobra_lista(list))
    print(__name__)