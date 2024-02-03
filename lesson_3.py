class Car: # чертеж
    #  __init__ - Конструктор, инструкция
    # self - сам объект
    # self.brand = атрибут/поле/свойства объекта
    wheels = 4 # атрибут/поле/свойства класса
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        self.is_start = False
        self.tank = 0

    def info(self):
        print(f"Бренд - {self.brand}, \nгод выпуска - {self.year}, \nцвет - {self.color}\n")

bmw = Car("m-5", 2021, "Black")
print(bmw.wheels)
bmw.info()


class SmartPhone:
    def __init__(self, model, sim_cards, battery):
        self.model = model # Публичный атрибут
        self._battery = battery 
        self.__sim_cards = sim_cards

    @property
    def sim_cards(self):
        return self.__sim_cards

    def info(self): # Публичный метод
        print(f"Бренд-{self.model}, сим карты-{self.__sim_cards}, батарейка-{self._battery}")
        self._gallery()
        # self.__password()

    def _gallery(self):
        print("Фотографии или галлерея")

    def __password(self):
        print("12345678")

    @property
    def password(self):
        return self.__password
    
mi = SmartPhone("note 10", ["MegaCom", "O!"], "500 Mach")
# mi.info()
# mi._gallery()
mi.password()
print(mi.sim_cards)
print(mi._battery)
print(mi.sim_cards)


def private(value):
    def test():

        print("Hello world!")
        value()
        print("Bye!")

    return test







@private
def hello():
    print("WTF!!!")
