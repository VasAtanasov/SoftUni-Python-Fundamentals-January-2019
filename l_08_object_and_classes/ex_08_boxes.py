import math


class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Box: {self.width:g}, {self.height:g}\nPerimeter: {self.get_perimeter():g}\nArea: {self.get_area():g}"


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        x_diff = abs(self.x - other_point.x)
        y_diff = abs(self.y - other_point.y)
        return math.sqrt(x_diff ** 2 + y_diff ** 2)


while True:
    line = input()
    if "end" == line:
        break

    points = [Point(*[int(number) for number in token.split(":")]) for token in line.split(" | ")]
    print(Box(points[0].distance_to(points[1]), points[0].distance_to(points[2])))
