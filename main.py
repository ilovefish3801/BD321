import json

if __name__ == "__main__":
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

        # new_list_product = []
        # for item in products:
        #     for color in item['colors']:
        #         if color.lower() == "чорний":
        #             new_list_product.append(item)
        #
        # print(new_list_product)

        # new_list_product = []
        # for item in products:
        #     if "Чорний" in item['colors']:
        #         new_list_product.append(item)
        #
        # print(new_list_product)

        # some_arr = [1, 2, 2, 3]
        # unique_val = []
        #
        # for el in some_arr:
        #     if el not in unique_val:
        #         unique_val.append(el)
        #
        # print(unique_val)
        # type_count = 0
        # for item in products:
        #
        #     for type in item['features']:
        #         type_check = type['value']
        #
        #         if type_check == "А++":
        #             type_count += 1
        # print(type_count)

        # for item in products:
        #     with open(f"single_product/{item['id']}.json", "w") as file:
        #         json.dump(item, file)

        # id = 13
        #
        # with open(f"single_product/{id}.json", "r") as file:
        #     product = json.load(file)
        #     print(product)

        prices = []

        for item in products:
            product_price = item['price'].replace(" ", '').replace(" ", '')
            product_price = int(product_price)
            prices.append(product_price)

        abs_price = sorted(prices)
        print(abs_price)
        desc_price = sorted(prices, reverse=True)
        print(desc_price)

        for item in range(5):
            print(desc_price[item])