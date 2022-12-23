def dict_add(dictionary, text):
    text = str(text).split(":")
    name, i_d, course = text[0], text[1], text[2]
    dictionary[i_d] = [name, course]

    return dictionary


def course_check(dictionary, text):
    dictionary = dict(dictionary)
    text = str(text).split("_")
    text = " ".join(text)
    res = ""
    for k, v in dictionary.items():
        if text in v:
            res += f"{v[0]} - {k}\n"

    return res


my_dict = {}
while True:
    text = input()
    if ":" not in text:
        print(course_check(my_dict, text))
        break

    dict_add(my_dict, text)