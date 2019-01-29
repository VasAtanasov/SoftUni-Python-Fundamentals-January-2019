class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def produce_sound(self, message):
        """Prints the message of classes inheriting tha Animal class"""
        print(message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, number_of_legs):
        Animal.__init__(self, name, age)
        self.number_of_legs = number_of_legs

    def produce_sound(self, **kwargs):
        super().produce_sound("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def __str__(self):
        return f"{super().__str__()}, Number Of Legs: {self.number_of_legs}"


class Cat(Animal):
    def __init__(self, name, age, intelligence_quotient):
        Animal.__init__(self, name, age)
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self, **kwargs):
        super().produce_sound("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def __str__(self):
        return f"{super().__str__()}, IQ: {self.intelligence_quotient}"


class Snake(Animal):
    def __init__(self, name, age, cruelty_coefficient):
        Animal.__init__(self, name, age)
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self, **kwargs):
        super().produce_sound("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def __str__(self):
        return f"{super().__str__()}, Cruelty: {self.cruelty_coefficient}"


def crete_class(class_type, params_array):
    create_functions = {
        "Dog": lambda params: Dog(params[0], int(params[1]), int(params[2])),
        "Cat": lambda params: Cat(params[0], int(params[1]), int(params[2])),
        "Snake": lambda params: Snake(params[0], int(params[1]), int(params[2])),
    }
    return create_functions[class_type](params_array)


animals = {}

while True:
    line = input()
    if "I'm your Huckleberry" == line:
        break

    tokens = line.split(" ")
    if "talk" == tokens[0] and tokens[1] in animals:
        animals[tokens[1]].produce_sound()
    else:
        animal_name = tokens[1]
        animals[animal_name] = crete_class(tokens[0], tokens[1:])


def print_animal_by_type(animal_type, collection):
    if len(collection) > 0:
        return "\n".join(map(str, filter(lambda animal: animal.__class__.__name__ == animal_type, collection)))
    return None


for key in ["Dog", "Cat", "Snake"]:
    result = print_animal_by_type(key, animals.values())
    if result:
        print(result)
