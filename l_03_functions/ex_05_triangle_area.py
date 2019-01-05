base = float(input())
height = float(input())


def calculate_triangle_area(base, height):
    return (base * height) / 2


area = calculate_triangle_area(base, height)

print(f'{area:.12g}')
