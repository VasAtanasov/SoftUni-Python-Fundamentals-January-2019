import re

emoji_regex = r"[:;*{}()\[\]cD][:;*{}()\[\]cD]"

input_string = input()

matches = re.finditer(emoji_regex, input_string)

happy_emoji = [":)", ":D", ";)", ":*", ":]", ";]", ":}", ";}", "(:", "*:", "c:", "[:", "[;"]
sad_emoji = [":(", "D:", ";(", ":[", ";[", ":{", ";{", "):", ":c", "]:", "];"]

happy_emoji_count = 0
sad_emoji_count = 0

for match in matches:
    emoji = match.group()
    if emoji in happy_emoji:
        happy_emoji_count += 1
    elif emoji in sad_emoji:
        sad_emoji_count += 1

happiness_index = happy_emoji_count

if sad_emoji_count > 0:
    happiness_index /= sad_emoji_count


def get_index_emoji(index):
    if index >= 2:
        return ":D"
    if index > 1:
        return ":)"
    if index == 1:
        return ":|"
    return ":("


print(f"Happiness index: {happiness_index:.2f} {get_index_emoji(happiness_index)}")
print(f"[Happy count: {happy_emoji_count}, Sad count: {sad_emoji_count}]")
