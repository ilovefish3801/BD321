import json

if __name__ == "__main__":
    with open("products.json", 'r', encoding="utf-8") as file:
        products = json.load(file)

    print(products)