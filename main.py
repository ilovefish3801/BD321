import json

if __name__ == "__main__":
    # arr = ["test!", "test2", "testR"]

    # count = 0
    # # 4 ways how to print arr items
    # for item in arr:
    #     print(item)
    # print("___________\n")
    #
    # while count < len(arr):
    #     print(arr[count])
    #     count += 1
    # print("___________\n")
    #
    # for item in range(len(arr)):
    #     print(arr[item])
    #
    # print("___________\n")
    #
    # test = [x for x in arr if x == "test!"]
    # # test 1 and 2 are the same but test 1 is smaller
    # test_2 = []
    # for i in arr:
    #     if i == "test!":
    #         test_2.append()

    # Sorting and Filtering

    # numbers = []
    # for i in range(1, 101, 1):
    #     numbers.append(i)
    # print(numbers)
    #
    # even_numbers = []
    # odd_numbers = []
    # for i in numbers:
    #     if i % 2 == 0:
    #         even_numbers.append(i)
    #     else:
    #         odd_numbers.append(i)
    # print(even_numbers)
    # print(odd_numbers)

    # sort

    # arr = [4, 56, 2, 6, 3, 89]
    # arr_two = arr.copy()
    # flag = True
    # while flag:
    #     flag = False
    #     status_check = True
    #     # Ефект бульбашки який можна замінити sorted або sort
    #     for i in range(len(arr) - 1):
    #         if arr[i] > arr[i + 1]:
    #             temp = arr[i]
    #             arr[i] = arr[i + 1]
    #             arr[i + 1] = temp
    #     for item in range(len(arr) - 1):
    #         if arr[item] > arr[item + 1] and flag == False:
    #             flag = True
    #
    # print(arr)
    # print(sorted(arr_two))
    #
    # # sort methods
    # # ABS
    # new_val = sorted(arr_two)
    # print(new_val)
    # arr_two.sort()
    # print(arr_two)
    #
    # # DESC
    # new_val_desc = sorted(arr_two, reverse=True)
    # print(new_val_desc)
    # arr_two.sort(reverse=True)
    # print(arr_two)
    #
    # str_arr = ["Jonny", "Ann", "Ketty", "Zak"]
    # # A-Z
    # sort_az_arr = sorted(str_arr)
    # print(sort_az_arr)
    # # Z-A
    # sort_za_arr = sorted(str_arr, reverse=True)
    # print(sort_za_arr)

    sort_title = ['hello']

    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

        products.sort(key=lambda x: x["title"])
        print(products)
        # for item in products:
        #     title = item['title']
        #
        #     sort_title.append(title)
        #
        #     sort_title_az = sorted(sort_title)
        #
        #     sort_title_za = sorted(sort_title, reverse=True)
        #
        # print(sort_title_za)
        # print(sort_title_az)

    with open("products_az.json", "w") as file:
        json.dump(products, file)