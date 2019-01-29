import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        x_diff = abs(self.x - other_point.x)
        y_diff = abs(self.y - other_point.y)
        return math.sqrt(x_diff ** 2 + y_diff ** 2)


point_a = Point(*list(map(float, input().split(" "))))
point_b = Point(*list(map(float, input().split(" "))))

print(f'{point_a.distance_to(point_b):.3f}')
