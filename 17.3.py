class Point:
    """Represents a point in a 2 dimensional space
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

point = Point(17, 12)

print point
