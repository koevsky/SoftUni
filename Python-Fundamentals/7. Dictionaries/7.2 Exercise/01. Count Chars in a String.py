def char_stats(text):
    text = str(text).split(" ")
    text = "".join(text)
    stats_dict = {}
    stats_dict = {x: text.count(x) for x in text if x not in stats_dict}
    res = ""
    for k, v in stats_dict.items():
        res += f"{k} -> {v}\n"

    return res


line = input()
print(char_stats(line))
