""""
    ТЕМА: цикл While
"""

# i = 3
#
# while i <= 15:
#     print(i)
#     i += 2

# while i <= 25:
#     i += 3
#     print(i)


#
# i = 45
#
# while i > 5:
#     print(i)
#     i //= 5


# while True:
#     x = int(input("x: "))
#     option = input("+, -, /, *       ")
#     y = int(input("y: "))
#
#     if option == "+":
#         print(x + y)
#     elif option == "-":
#         print(x - y)
#     elif option == "/":
#         if y == 0:
#             print("Infinity")
#         else:
#             print(x / y)
#     else:
#         print(x * y)
#
#     print()


# i = 0
#
#
# while i < 15:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

# while i < 100:
#     if i == 50:
#         print(i)
#         break
#     print(i)
#     i += 1


# while True:
#     name = input("Атыныз ким? ")
#
#     if name == "выход":
#         print("finished...")
#         break
#
#     print("Вы успешно зарегистрировались")


# i = 1
#
# while i < 11:
#     j = 0
#     while j < 11:
#         print(f"{i} * {j} = {i * j}")
#         j += 1
#     i += 1
#     print()


while True:
    year = input("Жылыныз канча? ")

    if year == "выход":
        print("Finished ...")
        break

    year = int(year)
    age = 2024 - year
    print("Азыркы учурдагы жашыныз:", age)
    print()



