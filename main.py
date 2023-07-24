def initials(surname, name, fathername):
    return f"{surname.capitalize()} {name[0].capitalize()}. {fathername[0].capitalize()}."


if __name__ == "__main__":
    print(initials("КожЕмякін", "Кирило", "РУсланович"))
