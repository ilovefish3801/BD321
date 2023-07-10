import json

if __name__ == "__main__":
    # with open("students_data.json", "r") as file:
    #     students = json.load(file)
    #     students.append(frame_student)
    #
    # with open("students_data.json", "w") as file:
    #     json.dump(students, file)

    # new_products = {
    # "id": 21,
    # "title": "Lorem ipsum dolor",
    # "price": 79.99,
    # "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut suscipit enim et mi.",
    # "category": "Lorem ipsum clothing",
    # "image": "https://hidepark.co.uk/cdn/shop/products/MensbrownleatherjacketHarry.jpg?v=1670510535",
    # "rating": {
    #   "rate": 3.8,
    #   "count": 600
    # }
    # }

    id_choice = int(input("Введіть id продукту, щоб видалити: "))
    title_choice = str(input("Введіть назву продукту: "))



    with open("products.json", "r") as file:
        products = json.load(file)
        print(products)
        for i in products:
            id = i['id']
            title = i['title']
            frame = [{
                "id": id_choice,
                "title": title_choice,
            }]
        print(type(frame))
        products.pop(frame)
    with open("products.json", "w") as file:
        json.dump(products, file)