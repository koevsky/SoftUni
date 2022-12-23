def odd_check(text):
    text = str(text).split(" ")
    text = [x.lower() for x in text]
    my_dict = {}
    my_dict = {x: text.count(x) for x in text if x not in my_dict.keys()}
    res = [k for k, v in my_dict.items() if v % 2 != 0]

    return " ".join(res)


line = input()
print(odd_check(line))

