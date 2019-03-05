class Technology:
    def __init__(self, name):
        self.__name = name
        self.__courses = {}

    @property
    def name(self):
        return self.__name

    def add(self, course, participants):
        if course not in self.__courses:
            self.__courses[course] = Course(name=course)

        self.__courses[course].add(participants)

    @property
    def total_participants(self):
        return sum(map(lambda c: c.participants, self.__courses.values()))

    def __get_sorted_participants(self):
        return "\n".join(map(str, sorted(self.__courses.values(), key=lambda c: -c.participants)))

    def __str__(self):
        return f"{self.__name} ({self.total_participants} participants):\n" \
            f"{self.__get_sorted_participants()}"


class Course:
    def __init__(self, name):
        self.__name = name
        self.__participants = 0

    def add(self, participants):
        self.__participants += participants

    @property
    def participants(self):
        return self.__participants

    def __str__(self):
        return f"--{self.__name} -> {self.__participants}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Course):
            return self.__name == other.__name
        return False


technologies = {}

while True:
    line = input()
    if "end" == line:
        break

    technology, courses_tokens = line.split(" - ")

    if technology not in technologies:
        technologies[technology] = Technology(technology)

    courses_tokens = [(course, int(participants)) for course, participants in
                      [token.split(':') for token in courses_tokens.split(", ")]]

    for course, participants in courses_tokens:
        technologies[technology].add(course, participants)

ordered = sorted(technologies.values(), key=lambda t: -t.total_participants)
print(f"Most popular: {ordered[0].name} ({ordered[0].total_participants} participants)")
print(f"Least popular: {ordered[-1].name} ({ordered[-1].total_participants} participants)")
for technology in sorted(technologies.values(), key=lambda t: -t.total_participants):
    print(technology)
