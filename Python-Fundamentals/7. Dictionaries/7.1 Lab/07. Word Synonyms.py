def syn_add(key, value, dictionary):
    dictionary = dict(dictionary)
    if key not in dictionary.keys():
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

    return dictionary


def dict_print(dictionary):
    dictionary = dict(dictionary)
    res = ""
    for k, v in dictionary.items():
        res += f"{k} - {', '.join(v)}\n"

    return res


num = int(input())
my_dict = {}
for i in range(num):
    key = input()
    value = input()
    my_dict = syn_add(key, value, my_dict)

print(dict_print(my_dict))