# # Множественное наследование

# class Car:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year

#     # def info(self):
#     #     print(f"бренд - {self.model}, год выпуска - {self.year}")

#     def __str__(self):
#         return f"бренд - {self.model}, год выпуска - {self.year}"

# class ElectricCar(Car):
#     def __init__(self, model, year, battery):
#         Car.__init__(self, model, year)
#         self.battery = battery

#     def __str__(self):
#         return super().__str__() + f", Заряд батарии - {self.battery}"

#     def drive(self):
#         print(f"Машина - {self.model} едет на электричестве")

# class FuelCar(Car):
#     def __init__(self, model, year, fuel_bank):
#         Car.__init__(self, model, year)
#         self.fuel_bank = fuel_bank

#     def drive(self):
#         print(f"Машина - {self.model} едет на топливе")

# class HybridCar(ElectricCar, FuelCar):
#     def __init__(self, model, year, battery, fuel_bank, speed):
#         super().__init__(model, year, battery)
#         FuelCar.__init__(self, model, year, fuel_bank)
#         self.speed = speed

#     def drive(self):
#         if self.speed > 60:
#             FuelCar.drive(self)
#         else:
#             ElectricCar.drive(self)

        

# tesla = ElectricCar("tesla - model x", 2024, 90)
# # tesla.info()
# tesla.drive()
# print(tesla)

# matiz = FuelCar("matiz - 3", 2020, 30)
# # matiz.info()
# matiz.drive()

# lexus = HybridCar("lexus - 300es", 2020, 40, 60, 10)
# # lexus.info()
# lexus.drive()

# Магические методы 

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    # def info(self):
    #     print(f"бренд - {self.model}, год выпуска - {self.year}")

    def __str__(self): # __str__ == print
        return f"бренд - {self.model},\n год выпуска - {self.year} это str"
        # return "Hello world"
    
    # def __repr__(self): # __repr__ == print
    #     return f"бренд - {self.model}, год выпуска - {self.year} это repr"

    def __call__(self, a, b):
        print(a + b)


    # Магисесие методы для арифметических действий

    def __add__(self, other): # +
        res = self.year + other.year
        return Car(self.model, res)

    def __sub__(self, other): # -
        res = self.year - other.year
        return Car(self.model, res)
    
    def __mul__(self, other): # *
        res = self.year * other.year
        return Car(self.model, res)
    
    def __floordiv__(self, other): # //
        res = self.year // other.year
        return Car(self.model, res)
    
    def __truediv__(self, other): # /
        res = self.year / other.year
        return Car(self.model, res)
    
    # Магические методы для операторов сравнения
    def __gt__(self, other): # больше чем (>) - greater than
        return self.year > other.year
    
    def __lt__(self, other): # меньше чем (<) - less than
        return self.year < other.year
    
    def __eq__(self, other): # равно (==) - equals
        return self.year == other.year
    # "=" - Знак присваивания
    # "==" - Знак равенства

    def __ne__(self, other): # не равно (!=) - not equals
        return self.year != other.year
    
    def __ge__(self, other): # больше или равно (>=) - greater or equals
        return self.year >= other.year
    
    def __le__(self, other): # меньше или равно (<=) - less or equals
        return self.year <= other.year
    
bmw = Car("bmw - m5", 2022)
mers = Car("bmw - m5", 2023)
# mers(2, 2)
# bmw.info()
print(bmw)
# Магисесие методы для арифметических действий
# print(bmw + mers)
# print(bmw - mers)
# print(bmw * mers)
# print(bmw / mers)
# print(bmw // mers)


# Магические методы для операторов сравнения
print(bmw > mers)
print(bmw < mers)
print(bmw == mers)
print(bmw != mers)
print(bmw >= mers)
print(bmw <= mers)