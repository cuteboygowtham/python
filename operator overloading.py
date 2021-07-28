#It means extended meaning beyond their predefined oeperational meeting.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


point1 = Point(2, 4)
point2 = Point(4, 6)

print(point1 + point2)