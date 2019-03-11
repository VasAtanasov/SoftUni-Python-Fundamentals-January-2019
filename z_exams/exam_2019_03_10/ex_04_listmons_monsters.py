from abc import ABC, abstractmethod


def is_integer(num):
    try:
        int(num)
        return True
    except Exception:
        return False


class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name, id, strength, ugliness):
        self.__name = name
        self.__id = id
        self.__strength = strength
        self.__ugliness = ugliness


class Hydralisk(BaseMonster):
    def __init__(self, name, id, strength, ugliness, range):
        BaseMonster.__init__(self, name, id, strength, ugliness)
        self.range = range

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, range):
        if is_integer(range):
            raise Exception("Range must be string")

        self.__range = range


class Zergling(BaseMonster):
    def __init__(self, name, id, strength, ugliness, speed):
        BaseMonster.__init__(self, name, id, strength, ugliness)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if not is_integer(speed):
            raise Exception("Speed must be integer")
        self.__speed = int(speed)


zergling_count = 0
hydralisk_count = 0
overall_strength = 0
overall_speed = 0

while True:
    line = input()
    if "stopAddingArmy" == line:
        break

    if line.startswith("BaseMonster"):
        print("Can't instantiate abstract class BaseMonster with abstract methods __init__")
        continue

    open_bracket = line.index("(")
    close_bracket = line.index(")")

    tokens = line[open_bracket + 1: close_bracket].split(", ")

    name = tokens[0]
    id = int(tokens[1])
    strength = int(tokens[2])
    ugliness = int(tokens[3])

    try:
        if line.startswith("Hydralisk"):
            if len(tokens) < 5:
                raise Exception("__init__() missing 1 required positional argument: 'range'")
            unit = Hydralisk(name, id, strength, ugliness, range=tokens[4])
            hydralisk_count += 1
            overall_strength += strength
        elif line.startswith("Zergling"):
            if len(tokens) < 5:
                raise Exception("__init__() missing 1 required positional argument: 'speed'")
            unit = Zergling(name, id, strength, ugliness, speed=tokens[4])
            zergling_count += 1
            overall_speed += unit.speed
            overall_strength += strength

    except Exception as ex:
        print(ex)

print(f"Overall speed of army: {overall_speed}\n"
      f"Overall stength: {overall_strength}\n"
      f"Hydralisk: {hydralisk_count}; Zergling: {zergling_count}")
