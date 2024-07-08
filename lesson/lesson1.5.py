"""
    ТЕМА: берилиш структуралары
    list, tuple
"""

"""list"""
my_list = ["Ermek", "Asan", "Bakyt", "Ali", "Гияc"]

"""index"""
# print(my_list[2])

"""Add"""
my_list.append("Sultan")
my_list.extend(["Жанайым", "Адинай"])
my_list.insert(0, "Таалай")
my_list.insert(1, "Адил")
# print(my_list)


"""Edit"""
my_list[2] = "Erlan"
my_list.reverse()
my_list.sort(reverse=True)
# print(my_list)

"""Delete"""
# my_list.remove("Erlan")
# my_list.pop(4)
# del my_list[2:]
# print(my_list)

"""Срезы [start:stop:step]"""
# print(my_list[:3])
# print(my_list[2:6:2])
# print(my_list[-1])


"""Tuple"""
# number = (1, 2, 3, 4, 5, 1)
# number_1 = 1,
#
# print(number.count(1))
# print(number.index(1))
# print(number[3])
