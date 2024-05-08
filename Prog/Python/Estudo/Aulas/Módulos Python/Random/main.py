import random
import string


inteiro = random.randint(10, 20)
# flutuante = random.uniform(10, 20)
flutuante = random.random()


lista = ['Jão', 'Zé', 'Bastião', 'Júlia', 'Joana']

# sorteio = random.choice(lista)

# sorteio = random.choices(lista, k=2)

sorteio = random.sample(lista, 2)

# random.shuffle(lista)

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))

print(senha)