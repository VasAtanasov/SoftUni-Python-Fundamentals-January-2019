input_text = input()
letters_type = input()

operation = {
    "LOWERCASE": lambda text: sum([ord(ch) for ch in list(text) if ch.isalpha() and ch.islower()]),
    "UPPERCASE": lambda text: sum([ord(ch) for ch in list(text) if ch.isalpha() and ch.isupper()])
}

print(f"The total sum is: {operation[letters_type](input_text)}")
