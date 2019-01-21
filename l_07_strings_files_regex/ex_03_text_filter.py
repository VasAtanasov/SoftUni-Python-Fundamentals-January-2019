banned_words = {word: "*" * len(word) for word in list(filter(None, input().split(" ")))}

text = input()

for word, replacement in banned_words.items():
    text = text.replace(word, replacement)

print(text)
