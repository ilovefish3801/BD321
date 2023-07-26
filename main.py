import json


def checkFile():
    try:
        with open("zoo.json", "r") as file:
            zoo = json.load(file)
    except Exception as err:
        Arr = {
            "animals": []
        }
        with open("zoo.json", "w") as file:
            json.dump(Arr, file)
        checkFile()






def addAnimal(breed, food):
    frame = {
        "breed": breed,
        "food": food,
    }
    zoo['animals'].append(frame)
    with open("zoo.json", "w", encoding="utf-8") as file:
        json.dump(zoo, file)


def searchAnimal(breed):
    for i in zoo['animals']:
        breedList = i['breed']
        foodList = i['food']
        if breed.lower() == breedList.lower():
            return foodList


# def numbersSum(firstNum, secondNum):
#     return firstNum + secondNum
#
#
# def createIntials(name, lastName, fathersName):
#     initials = False
#     try:
#         initials = f"{lastName.capitalize()} {name[0].upper()}. {fathersName[0].upper()}."
#     except Exception as err:
#         print("Сталась помилка в створенні ініціалів!")
#     return initials
#
# def runProgram():
#     numbersSum(1, 2)
#     print(createIntials("Kurulo", "Kozemiakin", "Ruslanovuc"))
#     temperature = int(input("Vvedit temperaturu: "))
#     if temperature > 0:
#         print("Teplo")
#     else:
#         print("Holodno")


if __name__ == "__main__":
    checkFile()
    flag = True
    while flag:
        print("\n 1 для додавання тварини в зоопарк\n", "2 для знаходження їжі за породою\n",
              "q щоб вийти з програми")
        choice = input("Введіть дію: ")

        if choice == "1":
            breed = input("Введіть породу: ")
            food = input("Введіть рекомендовану їжу для цієї породи ")
            addAnimal(breed, food)
        elif choice == "2":
            search = input("Введіть породу: ")
            print(searchAnimal(search))
        else:
            break

    # active = True
    # while active:
    #     try:
    #         runProgram()
    #     except Exception as err:
    #         print(err)
    #     finally:
    #         choice = input("Чи бажаєте продовжити користування ? Y/N:")
    #         if choice.lower() == "n":
    #             active = False

    # try:
    #     num = int("test")
    #     print(num)d
    # except Exception as err:
    #     print(err)
    # finally:
    #     print("Some text")
