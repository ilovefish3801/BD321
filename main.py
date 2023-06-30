if __name__ == "__main__":
    first_name = str(input("""Введіть своє ім'я: """))
    second_name = str(input("Введіть своє прізвище: "))
    full_name = f"{first_name}  {second_name}".lower()

    print(full_name.title())
    full_name = first_name + second_name
    full_name.lower()

    full_name.replace(" ", '')
    print(len(full_name))