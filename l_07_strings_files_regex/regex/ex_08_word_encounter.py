import re

input_tokens = input()
char = input_tokens[0]
n = int(input_tokens[1])

sentence_pattern = re.compile('^[A-Z].*?[?!.]$')
word_pattern = r'\w+'

words = []

while True:
    sentence = input()
    if sentence == 'end':
        break
    if not sentence_pattern.match(sentence):
        continue

    matches = re.findall(word_pattern, sentence)
    for match in matches:
        char_count = match.count(char)
        if char_count >= n:
            words.append(match)

print(", ".join(words))
