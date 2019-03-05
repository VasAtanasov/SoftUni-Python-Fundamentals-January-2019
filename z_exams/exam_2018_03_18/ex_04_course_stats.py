technologies = {}

while True:
    line = input()
    if "end" == line:
        break

    technology, courses_tokens = line.split(" - ")

    if technology not in technologies:
        technologies[technology] = {}

    courses_tokens = [(course, int(participants)) for course, participants in
                      [token.split(':') for token in courses_tokens.split(", ")]]

    for course, participants in courses_tokens:
        technologies[technology].setdefault(course, 0)
        technologies[technology][course] += participants


def get_total_participants(tech):
    return sum(tech.values())


technologies = sorted(technologies.items(), key=lambda key: -get_total_participants(key[1]))

print(f"Most popular: {technologies[0][0]} ({get_total_participants(technologies[0][1])} participants)")
print(f"Least popular: {technologies[-1][0]} ({get_total_participants(technologies[-1][1])} participants)")
for technology, courses in technologies:
    print(f"{technology} ({get_total_participants(courses)} participants):")

    for course, participants in sorted(courses.items(), key=lambda x: -x[1]):
        print(f"--{course} -> {participants}")
