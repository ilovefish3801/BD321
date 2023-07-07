if __name__ == "__main__":
    # students = [
    #     {
    #         "name": "John",
    #         "presense": None,
    #
    #     },
    #     {
    #         "name": "Jerry",
    #         "presense": None
    #     },
    #     {
    #         "name": "Jane",
    #         "presense": None
    #     },
    # ]
    # presense_count = 0
    #
    # for student in students:
    #     flag = True
    #     while flag:
    #         presense_choice = input(f"Чи є {student['name']} на занятті ? (Y/N)")
    #
    #         if presense_choice.lower() == "y":
    #             student['presense'] = True
    #             presense_count += 1
    #             flag = False
    #         elif presense_choice.lower() == "n":
    #             student['presense'] = False
    #             flag = False
    #         if flag:
    #             print("Ви обрали не вірне значення ! \n\n")
    #
    # print(f"Присутні: {presense_count}. Відсутні: {len(students) - presense_count}")

    # count_new_student = int(input("Скільки студентів хочете додати ? "))
    # for i in range(count_new_student):
    #
    #     name_student = input("""Введіть ім'я нового студента: """)
    #     frame_student = {
    #         "name": name_student,
    #         "presense": None
    #     }
    #     students.append(frame_student)
    #
    # print(students)

    # a = True
    # b = 0
    # while True:
    #     b += 1
    #     if b >= 100:
    #         continue
    #     elif b >= 105:
    #         break
    #     print(b)

    # b = 0
    # while b <= 100:
    #     question = int(input("Введіть число яке більше за 100: "))
    #     if question > 100:
    #         print("Ти вгадав")
    #         b = 101

    credit_data = {
        'user1': {
            'credit1': 5000,
            'credit2': 2000,
            'credit3': 10000
        },
        'user2': {
            'credit1': 3000,
            'credit2': 1500,
            'credit3': 8000
        },
        'user3': {
            'credit1': 7000,
            'credit2': 0,
            'credit3': 5000
        },
        'user20': {
            'credit1': 10000,
            'credit2': 5000,
            'credit3': 3000
        }
    }
    # credit_one_amount = 0
    # credit_two_amount = 0
    # credit_three_amount = 0
    # for i in credit_data:
    #     for credit in credit_data[i]:
    #         if credit == "credit1":
    #             credit_one_amount += credit_data[i][credit]
    #         elif credit == "credit2":
    #             credit_two_amount += credit_data[i][credit]
    #         elif credit == "credit3":
    #             credit_three_amount += credit_data[i][credit]
    #
    # print(" Заборговані по Кредиту1: ", credit_one_amount)
    # print(" Заборговані по Кредиту2: ", credit_two_amount)
    # print(" Заборговані по Кредиту3: ", credit_three_amount)
    max_debt = 0
    for i in credit_data:
        total_debt = 0
        for credit in credit_data[i]:
            total_debt += credit_data[i][credit]

        if max_debt < total_debt:
            max_debt = total_debt
            user_max_debt = i

        print(f"{i} --- {total_debt}")
    print(f"{user_max_debt} --- {max_debt}")