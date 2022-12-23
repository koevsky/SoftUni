def dict_add(key, value, dictionary):
    dictionary = dict(dictionary)
    if key in dictionary.keys():
        dictionary[key] += int(value)
    else:
        dictionary[key] = int(value)

    return dictionary


def dict_print(dictionary):
    dictionary = dict(dictionary)
    res = ""
    for k, v in dictionary.items():
        res += f"{k} -> {v}\n"

    return res


my_dict = {}
while True:
    resource = input()
    if resource == "stop":
        print(dict_print(my_dict))
        break
    quantity = int(input())

    my_dict = dict_add(resource, quantity, my_dict)
