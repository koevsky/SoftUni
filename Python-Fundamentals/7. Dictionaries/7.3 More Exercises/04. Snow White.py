def dwarf_add(text, dictionary):
    dictionary = dict(dictionary)
    text = str(text).split(" <:> ")
    dwarf_name, hat_color, physics = text[0], text[1], int(text[2])
    if hat_color not in dictionary.keys():
        dictionary[hat_color] = [[dwarf_name, physics]]
    else:
        if dwarf_name not in [x[0] for x in dictionary[hat_color]]:
            dictionary[hat_color].append([dwarf_name, physics])
        else:
            for x in dictionary[hat_color]:
                if x[0] == dwarf_name and x[1] < physics:
                    x[1] = physics
                    break

    return dictionary


def dwarf_sort(dictionary):
    dictionary = dict(dictionary)
    dictionary_sorted = dict(sorted(dictionary.items(), key=lambda x: (x[1], len(x[1])), reverse=True))


def dwarf_stats(sorted_dwarf_dict):
    pass



dwarf_dict = {}
while True:
    line = input()
    if line == "Once upon a time":
        dwarf_dict = dwarf_sort(dwarf_dict)
        dwarf_stats(dwarf_dict)
        break
    dwarf_dict = dwarf_add(line, dwarf_dict)







