text = input().lower()
searched_word = input().lower()
counter = 0

for i in range(len(text)):
    if text[i:i + len(searched_word)] == searched_word:
        counter += 1

print(counter)
