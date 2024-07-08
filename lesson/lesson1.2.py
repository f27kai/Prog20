"""
    ТЕМА: if elif else
"""

# x = 1000
#
# if x < 800:
#     print("Жок мен 800$га макул эмесмин")
# elif x < 999:
#     print("Жок мен 999$га макул эмесмин")
# elif x > 500 and x < 850:
#     print("Мен макул эмесмин")
# elif x == 1000:
#     print("Мен макулмун")
# else:
#     print("500$")

x = int(input("x: "))
option = input("+, -, /, *       ")
y = int(input("y: "))

if option == "+":
    print(x + y)
elif option == "-":
    print(x -y)
elif option == "/":
    if y == 0:
        print("Infinity")
    else:
        print(x / y)
else:
    print(x * y)


