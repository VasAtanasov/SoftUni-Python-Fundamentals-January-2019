state_integers = list(map(int, filter(None, input().split(" "))))
command_integers = list(map(int, filter(None, input().split(" "))))

for n in command_integers:
    absolute_value = abs(n)
    if absolute_value % 2 == 0:
        state_integers = [x * absolute_value if x % 2 == 0 else x for x in state_integers]
    else:
        state_integers = [x // absolute_value if x % 2 != 0 else x for x in state_integers]

    if n > 0:
        state_integers = [x + n if x > 0 else x for x in state_integers]
    elif n < 0:
        state_integers = [x + n if x < 0 else x for x in state_integers]

print(state_integers)
