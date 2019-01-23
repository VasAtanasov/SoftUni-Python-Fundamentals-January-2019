input_string = input()
LEFT_ARROW = "<"
RIGHT_ARROW = ">"
is_diamond = False

while LEFT_ARROW in input_string and RIGHT_ARROW in input_string:
    LEFT_ARROW_INDEX = input_string.index(LEFT_ARROW)
    RIGHT_ARROW_INDEX = input_string.index(RIGHT_ARROW)

    if LEFT_ARROW_INDEX > RIGHT_ARROW_INDEX:
        input_string = input_string[RIGHT_ARROW_INDEX + 1:]
        continue

    is_diamond = True

    sub_string = list(input_string[LEFT_ARROW_INDEX + 1:RIGHT_ARROW_INDEX])

    input_string = input_string[RIGHT_ARROW_INDEX + 1:]

    digits_sum = sum(map(int, filter(lambda num: num.isdigit(), sub_string)))

    print(f'Found {digits_sum} carat diamond')

if not is_diamond:
    print("Better luck next time")
