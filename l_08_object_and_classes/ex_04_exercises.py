class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

    def __str__(self):
        header = f"Exercises: {self.topic}\n" \
            f"Problems for exercises and homework for the \"{self.course_name}\" course @ SoftUni.\n" \
            f"Check your solutions here: {self.judge_contest_link}"
        if len(self.problems) == 0:
            return header
        else:
            header += "\n"
            for i in range(len(self.problems)):
                header += f'{i + 1}. {self.problems[i]}\n'
            return header.strip()


exercises = []

while True:
    line = input()
    if "go go go" == line:
        break
    tokens = list(filter(None, line.split(" -> ")))
    problems_array = list(filter(None, tokens[3].split(", ")))

    exercises.append(Exercise(tokens[0], tokens[1], tokens[2], problems_array))

for exercise in exercises:
    print(exercise)
