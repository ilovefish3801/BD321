import json

import math


def moneyExchange(amount):
    usd = 0.0272
    uah = amount * usd
    uah = round(uah, 2)
    return uah


def helloWorld():
    print("hello world !")


def filterLetter(letter, data):
    filtered_arr = []
    for item in data:
        title = item['title']
        if title[0].upper() == letter:
            filtered_arr.append(item)

    return filtered_arr


def listSquare(customList):
    newList = []
    for i in customList:
        newList.append(math.sqrt(i))
    return newList


def factorial(n):
    numFactorial = n
    while n > 1:
        n -= 1
        numFactorial = numFactorial * n

    return numFactorial


def isPolindrom(text):
    reversedText = text[::-1]
    if text == reversedText:
        return True
    else:
        return False


def cesarCode(txt, key=3):
    with open("alphabet.json", 'r') as file:
        alphabet_data = json.load(file)
    code_in_num = []
    for letter in txt:
        for l in alphabet_data:
            if alphabet_data[f"{l}"] == letter.lower():
                code_in_num.append(int(l) + int(key))
    code_word = ''
    for num in code_in_num:
        if num <= 26:
            code_word += alphabet_data[f"{num}"]
        else:
            code_word += alphabet_data[f"{num - 26}"]
    return code_word.capitalize()


if __name__ == "__main__":
    value = input("Vvedit slovo dlia perevirku: ")  # For polindrom
    enter_txt = "Python"

    # with open("products.json", 'r', encoding="utf-8") as file:
    #     products = json.load(file)

    # test = filterLetter("F", products)
    # print(test)

    # temp_arr = []
    # temp_k = []
    # for item in products:
    #     title = item['title']
    #     if title[0].upper() == "F":
    #         temp_arr.append(item)
    #     elif title[0].lower() == "k":
    #         temp_k.append(item)

    # print(temp_k)
    # print(temp_arr)
    # new_arr = []
    # for i in products:
    #     if len(i['title']) != 0:
    #         new_arr.append(i)
    #
    # print(new_arr)
    #
    # with open('products.json', 'w', encoding='utf-8') as file:
    #     json.dump(new_arr, file)

    # print(moneyExchange(5356))

    print(listSquare([4, 16, 64]))

    print(factorial(3))

    print(isPolindrom(value))

    print(cesarCode(enter_txt))