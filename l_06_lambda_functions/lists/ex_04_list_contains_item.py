input_numbers = [int(num) for num in input().split(' ')]
searched_element = int(input())

if searched_element in input_numbers:
    print("yes")
else:
    print("no")
