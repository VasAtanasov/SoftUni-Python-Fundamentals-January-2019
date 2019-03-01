import re

GLADIATOR_PATTERN = re.compile(r"^([^\n]+) -> ([^\n]+) -> ([0-9]+)$")
DUEL_PATTERN = re.compile(r"^([^\n]+) vs ([^\n]+)$")


class Gladiator:
    def __init__(self, name):
        self.__name = name
        self.__techniques = {}

    @property
    def total_skill(self):
        return sum(self.__techniques.values())

    @property
    def name(self):
        return self.__name

    @property
    def techniques(self):
        return self.__techniques

    def add(self, technique, skill):
        if technique not in self.__techniques:
            self.__techniques[technique] = skill

        if self.__techniques[technique] < skill:
            self.__techniques[technique] = skill

    def __str__(self):
        header = f"{self.name}: {self.total_skill} skill\n"
        output = []
        for technique, skill in sorted(self.__techniques.items(), key=lambda t: (-t[1], t[0])):
            output.append(f"- {technique} <!> {skill}")
        return header + "\n".join(output)


by_name = {}


def common_techniques(first, second):
    for opponent_one_technique in first.techniques:
        if opponent_one_technique in second.techniques:
            return True
    return False


while True:
    line = input()
    if "Ave Cesar" == line:
        break

    if GLADIATOR_PATTERN.match(line):
        gladiator, technique, skill = line.split(" -> ")

        if gladiator not in by_name:
            by_name[gladiator] = Gladiator(gladiator)

        by_name[gladiator].add(technique, int(skill))
    elif DUEL_PATTERN.match(line):
        opponent_one, opponent_two = line.split(" vs ")

        if opponent_one not in by_name or opponent_two not in by_name:
            continue

        if not common_techniques(by_name[opponent_one], by_name[opponent_two]):
            continue

        if by_name[opponent_one].total_skill > by_name[opponent_two].total_skill:
            del by_name[opponent_two]
        elif by_name[opponent_one].total_skill < by_name[opponent_two].total_skill:
            del by_name[opponent_one]

for gladiator in sorted(by_name.values(), key=lambda g: (-g.total_skill, g.name)):
    print(gladiator)
