def increase_even_by_two(number):
    if number % 2 == 0:
        return number + 2
    return number


def increase_odd_by_three(number):
    if number % 2 != 0:
        return number + 3
    return number


while True:
    line = input()
    if "stop playing" == line:
        break

    numbers = list(map(int, filter(None, line.split())))

    if len(set(numbers)) == len(numbers):
        numbers = sorted(list(map(increase_even_by_two, numbers)))
        print(f"Unique list: {','.join(map(str, numbers))}")
    else:
        numbers = sorted(list(map(increase_odd_by_three, numbers)))
        print(f"Non-unique list: {':'.join(map(str, numbers))}")

    print(f"Output: {(sum(numbers) / len(numbers)):.2f}")
