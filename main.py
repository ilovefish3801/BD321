if __name__ == "__main__":
    # arr = []
    #
    # for i in range(int(input("pochatok: ")), int(input("kinec: ")) + 1, 1):
    #     if i % 5 == 0 and i % 3 == 0:
    #         arr.append(i)
    # print(arr)

    star_value = 1
    end_value = 50

    simpleNum = []

    # Прості числа від 1 до 50
    # j - дільник
    for i in range(star_value, end_value):
        flag = True
        for j in range(star_value, end_value):
            if j != 1 and i != j and j <= i:
                result = i % j
                if result == 0:
                    flag = False
                    break
        if flag:
            simpleNum.append(i)
    print(simpleNum)