import math

width = float(input())
depth = float(input())
height = float(input())

number_of_barrels = int(input())

truck_volume = width * depth * height
barrels_count = 0

for i in range(number_of_barrels):
    r = float(input())
    h = float(input())
    barrel_volume = math.pi * r * r * h

    truck_volume -= barrel_volume

    if truck_volume <= 0:
        print(f"Truck is full. {barrels_count} on board!")
        exit()

    barrels_count += 1

print(f"All barrels on board. Capacity left - {truck_volume:.2f}.")
