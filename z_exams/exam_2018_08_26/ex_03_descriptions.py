import re

REGEX = {
    "name": r"name is (?P<name>[A-Z][A-Za-z]+ [A-Z][A-Za-z]+)",
    "age": r" (?P<age>[0-9]{2}) years",
    "date": r"on (?P<date>[0-9]{2}-[0-9]{2}-[0-9]{4})."
}


class Person:
    def __init__(self, full_name, age, birth_date):
        self.__full_name = full_name
        self.__age = age
        self.__birth_date = birth_date

    @property
    def full_name(self):
        return self.__full_name

    @property
    def age(self):
        return self.__age

    @property
    def birth_date(self):
        return self.__birth_date

    def __str__(self):
        return f"Name of the person: {self.full_name}.\n" \
            f"Age of the person: {self.age}.\n" \
            f"Birthdate of the person: {self.birth_date}."


db = []

while True:
    line = input()
    if "make migrations" == line:
        break
    if line[len(line) - 1] != '.':
        continue

    params = {}

    for requirement, regex in REGEX.items():
        match = re.search(regex, line)

        if not match:
            params = {}
            break

        if requirement == "age":
            age = int(match.group(requirement))
            if age <= 9 or age >= 100:
                break
            params["age"] = age
        elif requirement == "name":
            params["name"] = match.group(requirement)
        elif requirement == "date":
            params["date"] = match.group(requirement)

    if params:
        db.append(Person(full_name=params["name"], age=params["age"], birth_date=params["date"]))

if not db:
    print("DB is empty")
else:
    print("\n".join(map(str, db)))
