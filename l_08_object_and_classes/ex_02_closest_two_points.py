import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        x_diff = abs(self.x - other_point.x)
        y_diff = abs(self.y - other_point.y)
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def __str__(self):
        return f'({self.x:g}, {self.y:g})'


n = int(input())


def read_points():
    points_array = []
    for i in range(n):
        points_array.append(Point(*list(map(float, input().split(" ")))))
    return points_array


points = read_points()


def find_closest_points(points_array):
    min_dist = math.inf
    closest_pair = None
    for i in range(len(points_array) - 1):
        for j in range(i + 1, len(points_array)):
            point_a = points_array[i]
            point_b = points_array[j]
            distance = point_a.distance_to(point_b)
            if distance < min_dist:
                min_dist = distance
                closest_pair = (point_a, point_b, distance)
    return closest_pair


a, b, dist = find_closest_points(points)

print(f'{dist:.3f}')
print(f'{a}')
print(f'{b}')
