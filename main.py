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

    targetElement = someArray.index(1.6)
    print(targetElement)
    someArray[targetElement] = "test3"
    print(someArray)

    someArray.reverse()
    print(someArray)

    someArray.clear()
    print(someArray)

    a = [1]
    b = a
    a[0] += 1
    print(a)
    print(b)

    tempDist = {
        "name": {
            "test": "text"
        }

    }

    print(tempDist["name"])

    name = input("Vvedit ima: ")
    surname = input("Vvedit prizvushce: ")
    fathers_name = input("Vvedit pobatkovi: ")
    city = input("Vvedit svoe misto: ")
    address = input("Vvedit svij adress: ")
    phoneNum = input("Vvedit svij nomer telefonu")
    index = input("Vvedit svij index: ")

    name = name.title()
    surname = surname.title()
    fathers_name = fathers_name.title()

    personal_data = {
        "name": name,
        "surname": surname,
        "faters_name": fathers_name,
        "city_info": city,
        "adress_info": address,
        "index_info": index,
        "phoneNum_info": phoneNum,
        "pib": f"{surname} {name} {fathers_name}"
    }

    personal_data["age"] = 18

    print(personal_data)
