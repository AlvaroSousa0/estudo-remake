def fizzbuzz(x):
    x = int(x)
    if x % 5 == 0 and x % 3 == 0:
        return 'FizzBuzz'
    elif x % 5 == 0:
        return 'Buzz'
    elif x % 3 == 0:
        return 'Fizz'

num = input('Digite um número inteiro. ')
print(fizzbuzz(num))