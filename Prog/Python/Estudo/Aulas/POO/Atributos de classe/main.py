class A:
    vc = 123

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()
A.vc = 'alterado'

print

print(a1.vc)
print(a2.vc)
print(A.vc)