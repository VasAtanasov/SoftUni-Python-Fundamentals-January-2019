from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise Exception("Invalid input!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not age.strip() or int(age) <= 0:
            raise Exception("Invalid input!")
        self.__age = int(age)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if not gender.strip():
            raise Exception("Invalid input!")
        self.__gender = gender

    @abstractmethod
    def produce_sound(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}\n{self.name} {self.age} {self.gender}\n{self.produce_sound()}"


class Dog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Woof!"


class Frog(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def __init__(self, name, age, gender):
        Animal.__init__(self, name, age, gender)

    def produce_sound(self):
        return "Meow meow"


class Tomcat(Cat):
    def __init__(self, name, age):
        Cat.__init__(self, name, age, gender="Male")

    def produce_sound(self):
        return "MEOW"


class Kitten(Cat):
    def __init__(self, name, age):
        Cat.__init__(self, name, age, gender="Female")

    def produce_sound(self):
        return "Meow"


def get_animal(animal_type, name, age, gender):
    types = {
        "Cat": Cat(name, age, gender),
        "Dog": Dog(name, age, gender),
        "Frog": Frog(name, age, gender),
        "Tomcat": Tomcat(name, age),
        "Kitten": Kitten(name, age),
    }
    if animal_type not in types.keys():
        raise Exception("Invalid input!")
    return types[animal_type]


while True:
    line = input()
    if "Beast!" == line:
        break
    name, age, gender = input().split()
    try:
        print(get_animal(line, name, age, gender))
    except Exception as exe:
        print(exe)
