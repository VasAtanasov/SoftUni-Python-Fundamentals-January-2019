import re
from abc import ABC, abstractmethod


class Human(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: firstName")
        if len(first_name) <= 3:
            raise Exception("Expected length at least 4 symbols! Argument: firstName")
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name[0].isupper():
            raise Exception("Expected upper case letter! Argument: lastName")
        if len(last_name) <= 2:
            raise Exception("Expected length at least 3 symbols! Argument: lastName")
        self.__last_name = last_name

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\n"


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        Human.__init__(self, first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
        is_allowed = bool(re.match("^[A-Za-z0-9]*$", faculty_number))
        length = len(faculty_number)

        if length < 5 or length > 10 or not is_allowed:
            raise Exception("Invalid faculty number!")
        self.__faculty_number = faculty_number

    def __str__(self):
        return Human.__str__(self) + f"Faculty number: {self.faculty_number}"


class Worker(Human):
    def __init__(self, first_name, last_name, week_salary, hours_per_day):
        Human.__init__(self, first_name, last_name)
        self.week_salary = float(week_salary)
        self.hours_per_day = float(hours_per_day)

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, week_salary):
        if week_salary <= 10:
            raise Exception("Expected value mismatch! Argument: weekSalary")
        self.__week_salary = week_salary

    @property
    def hours_per_day(self):
        return self.__hours_per_day

    @hours_per_day.setter
    def hours_per_day(self, hours_per_day):
        if hours_per_day < 1 or hours_per_day > 12:
            raise Exception("Expected value mismatch! Argument: workHoursPerDay")
        self.__hours_per_day = hours_per_day

    @property
    def salary_per_hour(self):
        return (self.week_salary / 5) / self.hours_per_day

    def __str__(self):
        return Human.__str__(self) + f"Week Salary: {self.week_salary:.2f}\n" \
            f"Hours per day: {self.hours_per_day:.2f}\n" \
            f"Salary per hour: {self.salary_per_hour:.2f}"


try:
    student = Student(*list(input().split()))
    worker = Worker(*list(input().split()))
    print(student)
    print()
    print(worker)
except Exception as exe:
    print(exe)
