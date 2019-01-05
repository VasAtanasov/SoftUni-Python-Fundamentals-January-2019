def get_sing_of_number(number):
    return "negative" if number < 0 else "zero" if number == 0 else "positive"


num = int(input())
print(f'The number {num} is {get_sing_of_number(num)}.')
