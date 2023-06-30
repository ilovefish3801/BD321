if __name__ == "__main__":
    # first_name = str(input("""Введіть своє ім'я: """))
    # second_name = str(input("Введіть своє прізвище: "))
    # full_name = f"{first_name}  {second_name}".lower()
    #
    # print(full_name.title())
    # full_name = first_name + second_name
    # full_name.lower()
    #
    # full_name.replace(" ", '')
    # print(len(full_name))

    someArray = [1, "test", True, 1.6, "hey"]

    print(someArray[4])

    someArray.append(2)

    print(someArray)

    someArray.pop(1)

    targeteElement = someArray.index(1.6)
    print(targeteElement)
    someArray[targeteElement] = "test3"
    print(someArray)

    someArray.reverse()
    print(someArray)

    someArray.clear()
    print(someArray)