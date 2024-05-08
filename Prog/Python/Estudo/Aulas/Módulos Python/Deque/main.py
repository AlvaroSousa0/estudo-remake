# livros = list()

# livros.append('Livro 1')
# livros.append('Livro 2')
# livros.append('Livro 3')
# livros.append('Livro 4')            ####  Pilha - LIFO - last in first out
# livros.append('Livro 5')
# livros.append('Livro 6')
# print(livros)
# removidos = livros.pop()
# print(livros, removidos)     



from collections import deque
from time import sleep

fila = deque(maxlen=10)

for i in range(100):
    fila.append(i)
    sleep(1)
    print(fila)


# fila.extend([1, 2, 3, 4])
# print(fila)
# fila.append(5)
# print(fila)
# fila.append(6)
# print(fila)


# fila.append('João')
# fila.append('Mateus')
# fila.append('Julia')
# fila.append('Carlos')
# fila.append('Joana')
# print(fila)
# fila.popleft()
# print(fila)
# fila.popleft()
# print(fila)

