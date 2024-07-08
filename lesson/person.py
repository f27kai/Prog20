def person_name(name, surname, age):
    print(f"Name: {name}\n"
          f"Surname: {surname}\n"
          f"Age: {age}")


def calculator():
    while True:
        x = int(input("x: "))
        option = input("+, -, /, *       ")
        y = int(input("y: "))

        if option == "+":
            print(x + y)
        elif option == "-":
            print(x - y)
        elif option == "/":
            if y == 0:
                print("Infinity")
            else:
                print(x / y)
        else:
            print(x * y)
        print()