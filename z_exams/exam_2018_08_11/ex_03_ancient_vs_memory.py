array = []

while True:
    line = input()
    if "DEBUG" == line:
        break

    array += list(map(int, filter(None, line.split(" "))))

for i in range(len(array) - 6):
    if array[i] == 32656 and array[i + 1] == 19759 and array[i + 2] == 32763:
        n = array[i + 4]
        start = i + 6
        end = start + n
        sequence = array[start:end]
        print("".join(list(map(chr, sequence))))
