if __name__ == "__main__":
    # first_name = str("John")
    # second_name = str("Doe")
    # third_name = str("Patrick")
    #
    # user_data = {"name": first_name, "fathersName": third_name, "surname": second_name,
    #              "pib": f"{second_name.title()} {first_name[0].upper()}. {third_name[0].upper()}.", 'age': 26}
    #
    # # print(third_name[::-1])
    #
    # print(user_data)
    #
    # arr_names = ("John", "Jerry", "Simon")
    #
    # arr_surnames = {"Doe", "Lee", "Chan"}
    #
    # arr_surnames.add('test')
    # arr_surnames.remove('Lee')
    #
    # print(arr_surnames)

    users = [
        {
            "name": "John",
            "age": 31
        },
        {
            "name": "Jane",
            "age": 27,
            "family": {
                'mom': {
                    "name": "Sophie",
                    "age": 54,
                },
                'dad': {
                    "name": "Johny",
                    "age": 56,
                },

            },
        },
        {
            "name": "Jack",
            "age": 15
        },
        {
            "name": "Jonathan",
            "age": 38
        },
    ]

    # print(users[2]['name'], users[2]['age'])
    # print(users[1]["family"])

    # temp_age = users[1]['age']
    # temp_name = users[1]['name']
    #
    # if temp_age >= 18:
    #     print(temp_name, "you are 18 or older congrats !")
    # elif temp_name <= 18:
    #     print(temp_name, "you are a child I wont sell you any drinks >:(")

    # degrees = int(input("Введіть температуру: "))
    #
    # if degrees > 0:
    #     print("Тепло вдягнись легше")
    # elif degrees < 0:
    #     print("Ух, як холодно. Вдягни щось тепле")
    # else:
    #     print("Вдягнись як хочеш")

    print("""1-Цельсії""")
    print("""2-Кельвіни""")
    print("""3-Фарантгейти""")

    theDegrees = int(input("Введіть градуси: "))
    degrees_Type = int(input("Введіть вид градусу: "))

    if degrees_Type == 1:
        print(theDegrees * 1.8 + 32, "Фарантгейтів")
        print(theDegrees + 273.15, "Кельвінів")
    elif degrees_Type == 2:
        print(theDegrees - 273.15, "Цельсіїв")
        print((theDegrees - 273.15) * 1.8000 + 32.00, "Кельвінів")
    else:
        print(theDegrees - 32 / 1.8, "Цельсіїв")
        print(theDegrees - 32 / 1.8 + 273.75, "Кельвінів")
