def divide(n1, n2):
    # try:
    #     return n1 / n2
    # except ZeroDivisionError as erro:
    #     print('Log: ',erro)
    #     raise
    if n2 == 0:
        raise ValueError('n2 não pode ser zero.')
    return n1 / n2
try:
    print(divide(2, 0))
except ValueError as erro:
    print('Log: ',erro)