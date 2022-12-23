def phonebook_add(text, dictionary):
    dictionary = dict(dictionary)
    text = str(text).split("-")
    name, number = text[0], text[1]
    dictionary[name] = number

    return dictionary


def phonebook_check(name, dictionary):
    dictionary = dict(dictionary)
    res = ""
    if name in dictionary.keys():
        res = f"{name} -> {dictionary[name]}"
    else:
        res = f"Contact {name} does not exist."

    return res


my_dict = {}
while True:
    line = input()
    if line.isdigit():
        for _ in range(int(line)):
            person = input()
            print(phonebook_check(person, my_dict))
        break

    my_dict = phonebook_add(line, my_dict)
