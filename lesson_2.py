# Основные принципы ООП

class Animals: # Родителоьский класс и Абстрактный класс
    def __init__(self,  value, classes, color, age):
        self.breed = value
        self.classes = classes
        self.color = color
        self.age = age

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}")

    def make_sound(self):
        pass

# dog = Animals("Долматинец", "Млекопитающие", "Черный", 2)
# print(f" порода-{dog.breed}, {dog.classes}, {dog.color}, {dog.age}")
# dog.info()

# cow = Animals("Ярославская", "Парнокопытные", "Белый", 12)
# print(f" порода-{cow.breed}, {cow.classes}, {cow.color}, {cow.age}")
# cow.info()

# class Snake(Animals):
#     pass

# anakonda = Snake("anakonda", "Чешуйчатые", "Розовый", 16)
# anakonda.info()

class Dog(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.paws = 4

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во лап-{self.paws}")

    def make_sound(self):
        print("Gaf-Gaf")


class Cat(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.paws = 4

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во лап-{self.paws}")

    def make_sound(self):
        print("Meow")


class Cow(Animals): # Дочерний класс
    def __init__(self, breed, classes, color, age):
        super().__init__(breed, classes, color, age)
        self.horns = 2

    def info(self):
        print(f"{self.breed}, {self.classes}, {self.color}, {self.age}, кол-во рог-{self.horns}")

    def make_sound(self):
        print("Moo")


dog = Dog("Haski", "млекопитающий", "Grey", 3)
dog.make_sound()

cat = Cat("Ryjik", "млекопитающий", "Orange", 1)
cat.make_sound()

cow = Cow("Murka", "млекопитающий", "Black", 15)
cow.make_sound()


