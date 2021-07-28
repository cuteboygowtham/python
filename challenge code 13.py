class Point:
    def __init__(self, x):
        self.x = x


    def __mul__(self, other):
        x = self.x + other.x
        return x

mul1 = Point(4)
mul2 = Point(3)
print(mul1 * mul2)
