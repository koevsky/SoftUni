import os


def create(lst):
    f_n = open(lst[0], "w")
    f_n.close()


def add(lst):
    name, content = lst
    with open(name, "a") as file:
        file.write(f"{content}\n")


def replace(lst):
    name, old, new = lst
    try:
        with open(name, "r") as f:
            data = f.read()

        data = data.replace(old, new)

        with open(name, "w") as f:
            f.write(data)
    except:
        print("An error occurred")


def delete(lst):
    name = lst[0]
    try:
        os.remove(name)
    except:
        print("An error occurred")


while True:

    line = input()
    if line == "End":
        break

    key_word, *args = line.split("-")

    if key_word == "Create":
        create(args)

    elif key_word == "Add":
        add(args)

    elif key_word == "Replace":
        replace(args)

    elif key_word == "Delete":
        delete(args)


