"""
    ТЕМА: Инкапсуляция, Полиморфизм
"""
"""
    public
    protected
    private
"""
#
# class Car:
#
#     def __init__(self, marka, year, model):
#         self.__marka = marka
#         self.__year = year
#         self.__model = model
#
#     def get_marka(self):
#         return self.__marka
#
#     def set_marka(self, newmarka):
#         self.__marka = newmarka
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, newyear):
#         self.__year = newyear
#
#     def get_model(self):
#         return self.__model
#
#     def set_model(self, newmodel):
#         self.__model = newmodel
#
#     def get_info(self):
#         print(f"Marka: {self.get_marka()}\n"
#               f"Year: {self.get_year()}\n"
#               f"Model: {self.get_model()}")
#
# mercedes = Car("Mercedes", 2023, "S-class cabrio")
# mercedes.get_info()
# print()
#
# lexus = Car("Lexus", 2020, "LEXUS LS")
# lexus.set_model("LEXUS LX")
# lexus.get_info()


class Animal:

    def __init__(self, type, height, city):
        self.__type = type
        self.__height = height
        self.__city = city

    def get_type(self):
        return self.__type

    def set_type(self, newtype):
        self.__type = newtype

    def get_height(self):
        return self.__height

    def set_height(self, newheight):
        self.__height = newheight

    def get_city(self):
        return self.__city

    def set_city(self, newcity):
        self.__city = newcity

    def voice(self):
        pass

    def get_info(self):
        print(f"Type: {self.get_type()}\n"
              f"Height: {self.get_height()}\n"
              f"City: {self.get_city()}")

class Cat(Animal):
    def __init__(self, type, height, city, pets):
        super().__init__(type, height, city)
        self.__pets = pets

    def get_pets(self):
        return self.__pets

    def set_pets(self, newpets):
        self.__pets = newpets

    def voice(self):
        print("The cat meows")

    def get_info(self):
        super().get_info()
        print(f"Pets: {self.get_pets()}\n")


class Кangaroo(Animal):

    def __init__(self, type, height, city, eat):
        super().__init__(type, height, city)
        self.__eat = eat

    def get_eat(self):
        return self.__eat

    def set_eat(self, neweat):
        self.__eat = neweat

    def voice(self):
        print("The sound a kangaroo makes can be described as a 'grunting' noise.")

    def get_info(self):
        super().get_info()
        print(f"Eat: {self.get_eat()}\n")

cat = Cat("Cat", "5cm", "Bishkek", "Yes")
cat.get_info()
cat.voice()
print()
kangaroo = Кangaroo("Kangaroo", "1.60cm", "Afrika", "fruits and grass")
kangaroo.get_info()
kangaroo.voice()