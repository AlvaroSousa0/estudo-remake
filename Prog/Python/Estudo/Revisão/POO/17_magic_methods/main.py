class Ponto:
    def __init__(self, x ,y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name} x={self.x}, y={self.y}'

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other    

p1 = Ponto(1, 2)
p2 = Ponto(345, 123)
print(p2 < p1)