print(", ".join(dict.fromkeys(sorted([word for word in input().split(" ") if word == word[::-1]], key=str.lower))))
