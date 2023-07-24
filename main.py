import json

with open("users.json", "r") as file:
    usersList = json.load(file)


def initials(first_name, last_name, fathername):
    return f"{last_name.capitalize()} {first_name[0].upper()}. {fathername[0].upper()}."


def fib(firstNumber, secondNumber, finalNumber):
    fibArr = []
    while secondNumber <= finalNumber:
        nextNumber = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = nextNumber
        if secondNumber <= finalNumber:
            fibArr.append(nextNumber)

    return fibArr


def moneyWithdraw(id, amount):
    for i in usersList['accounts']:
        identefication = i['id']
        moneyAmount = i['balance']

        if id == identefication and amount <= moneyAmount:
            moneyAmount = moneyAmount - amount
            print(moneyAmount)
            


if __name__ == "__main__":
    # flag = False
    # while flag:
    #     print("\n Створити новий рахунок - 1\n", "Зняти кошти з рахунку - 2\n", "Поповнити рахунок - 3\n",
    #           "Перенести кошти з одного рахунку до іншого - 4\n", "Перевірити баланс рахунку - 5\n",
    #           "Вийти з програми - q")
    #     choice = int(input("shco vu hocete zrobutu ? "))
    #     if choice == 1:
    #         name = input("vvedit ima vlasnuka: ")
    #         startingBalance = int(input("vvedit pocatkovuj balanc: "))
    #         name = name.title()
    #
    #         accountId = 0
    #
    #         for i in usersList:
    #             for a in usersList[i]:
    #                 newId = a['id']
    #                 if accountId < newId:
    #                     accountId = newId
    #
    #         frame = {
    #             "id": accountId + 1,
    #             "owner_name": name,
    #             "balance": startingBalance
    #         }
    #
    #         usersList['accounts'].append(frame)
    #
    #         # with open('users.json', "w") as file:
    #         #     json.dump(usersList, file)
    #     elif choice == 2:
    #         userId = int(input("vvedit ID rahynky: "))

    moneyWithdraw(2, 1000)
    print(usersList)
