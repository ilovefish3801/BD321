if __name__ == "__main__":
    # temperature = int(input("Введіть температуру: "))

    # if 10 >= temperature > -10:
    #     print("Прохолодно")
    # elif temperature > 10:
    #     print("Тепло")
    # else:
    #     print("Холодно")

    # kisnevo_riven = int(input("Введіть рівень кисню: "))

    # if kisnevo_riven > 18 and 35 >= temperature >= 25:
    #     print("Можна відкрити вікно")
    # else:
    #     print("Не можна відкривати вікно")

    # age = int(input("Скільки вам років ? "))
    # income = int(input("Який у вас дохід ? "))
    # employed_input = input("Ви маєте стабільне працевлаштування ? ")
    # blacklist_input = input("Ви знаходитесь в списку небажаних позичальників ? ")
    # employed = bool
    # blacklist = bool
    #
    # if employed_input == "так":
    #     employed = True
    # else:
    #     employed = False
    #
    # if blacklist_input == "ні":
    #     blacklist = False
    # else:
    #     blacklist = True
    #
    # if employed == True and blacklist == False and 18 < age < 65 and income >= 25000:
    #     print("Вам допустимий кредит")
    # else:
    #     print("Вам не допустимий кредит")

    friend_check = input("Ви привели з собою друга ?")
    friend_credit = bool
    if friend_check == "так":
        friend_credit = True
    else:
        friend_credit = False

    





    age = int(input("Скільки вам років ? "))
    income = int(input("Який у вас дохід ? "))
    category = " "
    credit_time = int(input("Введіть час кредиту (в місяцях): "))
    credit_amount = int(input("Введіть суму кредиту: "))
    credit_percent = credit_time / 100 * 2
    credit_sum = credit_amount * credit_percent
    credit_sum = credit_sum + credit_amount
    credit_per_month = credit_sum / credit_time

    if 18 <= age <= 25 and income < 20000:
        category = "Студеньський кредит"
    elif 26 <= age <= 40 and 20000 < income < 40000:
        category = "Особистий кредит"
    elif 41 <= age <= 60 and income > 40000:
        category = "Поточний кредит"
    else:
        category = "Недоступний кредит"




    max_credit = (income * age) / 4
    print("Максимальний допустимий кредит: ", max_credit)
    print(category)
    print(round(credit_per_month, 1))

