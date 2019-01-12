text = input()

letters = {}

for i in range(0, len(text)):
    letter = text[i]
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

print(("\n".join([f'{letter} -> {letters[letter]}' for letter in letters.keys()])))
