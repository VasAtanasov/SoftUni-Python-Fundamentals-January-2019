value = input()
paramOne = input()
paramTwo = input()
result = {
    'int': lambda a, b: a if int(a) > int(b) else b,
    'char': lambda a, b: a if ord(a) > ord(b) else b,
    'string': lambda a, b: a if a > b else b,
}[value]

print(result(paramOne, paramTwo))
