import re

fish_pattern = r"(?P<tail>[>]{0,})<(?P<body>[(]{1,})(?P<state>['x-])>"
char_length = 2

input_line = input()

state_type = {
    "'": "Awake",
    "-": "Asleep",
    "x": "Dead"
}


def get_body_type(body_word):
    length = char_length * len(body_word)
    if len(body_word) > 10:
        return f"Long ({length} cm)"
    if len(body_word) > 5:
        return f"Medium ({length} cm)"
    return f"Short ({length} cm)"


def get_tail_type(tail_word):
    length = char_length * len(tail_word)
    if len(tail_word) > 5:
        return f"Long ({length} cm)"
    if len(tail_word) > 1:
        return f"Medium ({length} cm)"
    if len(tail_word) == 1:
        return f"Short ({length} cm)"
    return "None"


matches = re.finditer(fish_pattern, input_line)
is_match = False

rank = 1
for match in matches:
    is_match = True
    tail = match.group("tail")
    body = match.group("body")
    state = match.group("state")
    print(f"Fish {rank}: {match.group()}")
    print(f"  Tail type: {get_tail_type(tail)}")
    print(f"  Body type: {get_body_type(body)}")
    print(f"  Status: {state_type[state]}")
    rank += 1

if not is_match:
    print("No fish found.")

