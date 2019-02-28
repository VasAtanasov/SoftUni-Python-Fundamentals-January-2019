class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception("Name's length should not be less than 3 symbols!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        print('setter person')
        if age <= 0:
            raise Exception("Age should not be negative number!")
        self.__age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'


class Child(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        print('setter child')
        if age > 15:
            raise Exception("Child's age must be less than 15!")
        if age < 0:
            raise Exception('Age must be positive!')
        self.__age = age


try:
    person = Child(input(), int(input()))
    print(person)
except Exception as exe:
    print(exe)
