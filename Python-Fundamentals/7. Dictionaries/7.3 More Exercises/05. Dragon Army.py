def dragon_add(text, dictionary):
    dictionary = dict(dictionary)
    text = str(text).split(" ")
    dragon_type, name, damage, health, armor = text[0], text[1], text[2], text[3], text[4]
    if "null" not in text:
        dragon_type, name, damage, health, armor = text[0], text[1], int(text[2]), int(text[3]), int(text[4])
    else:
        for x in range(len(text)):
            if x == 2 and text[x] == "null":
                text[x] = 45
            elif x == 3 and text[x] == "null":
                text[x] = 250
            elif x == 4 and text[x] == "null":
                text[x] = 10
        dragon_type, name, damage, health, armor = text[0], text[1], int(text[2]), int(text[3]), int(text[4])

    if dragon_type not in dictionary.keys():
        dictionary[dragon_type] = {name:{"damage": damage, "health": health, "armor": armor}}
    else:
        if name not in dictionary[dragon_type].keys():
            dictionary[dragon_type][name] = {"damage": damage, "health": health, "armor": armor}
        else:
            dictionary[dragon_type][name] = {"damage": damage, "health": health, "armor": armor}

    return dictionary


def dragon_stats(dictionary):
    dictionary = dict(dictionary)
    res = ""
    for d_type in dictionary.keys():
        av_damage = sum([dictionary[d_type][name]["damage"] for name in dict(dictionary[d_type]).keys()]) / len(dictionary[d_type])
        av_health = sum([dictionary[d_type][name]["health"] for name in dict(dictionary[d_type]).keys()]) / len(dictionary[d_type])
        av_armor = sum([dictionary[d_type][name]["armor"] for name in dict(dictionary[d_type]).keys()]) / len(dictionary[d_type])
        names_sorted = dict(sorted(dict(dictionary[d_type]).items(), key=lambda x: x[0]))
        res += f"{d_type}::({av_damage:.2f}/{av_health:.2f}/{av_armor:.2f})\n"
        for k, v in names_sorted.items():
            res += f"-{k} -> damage: {v['damage']}, health: {v['health']}, armor: {v['armor']}\n"

    return res


n = int(input())
dragon_dict = {}
for _ in range(n):
    line = input()
    dragon_dict = dragon_add(line, dragon_dict)

print(dragon_stats(dragon_dict))
