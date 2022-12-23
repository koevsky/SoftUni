def rate(plt_dict, plt, rty):
    plt_dict = dict(plt_dict)
    if plt in plt_dict.keys():
        plt_dict[plt][1].append(int(rty))
    else:
        print("error")
    return plt_dict


def update(plt_dict, plt, new_rarity):
    plt_dict = dict(plt_dict)
    if plt in plt_dict.keys():
        plt_dict[plt][0] = int(new_rarity)
    else:
        print("error")
    return plt_dict


def reset(plt_dict, plt):
    if plt in plt_dict.keys():
        plt_dict[plt][1].clear()
    else:
        print("error")
    return plt_dict


plants_dict = {}
n = int(input())
for _ in range(n):
    plant = input().split("<->")
    p_type, rarity = plant[0], plant[1]
    plants_dict[p_type] = [int(rarity), []]

while True:
    line = input()
    if line == "Exhibition":
        break
    cmd = line.split(": ")
    if cmd[0] == "Rate":
        info = cmd[1].split(" - ")
        plant, rating = info[0], info[1]
        plants_dict = rate(plants_dict, plant, rating)
    elif cmd[0] == "Update":
        info = cmd[1].split(" - ")
        plant, new_rty = info[0], info[1]
        plants_dict = update(plants_dict, plant, new_rty)
    elif cmd[0] == "Reset":
        info = cmd[1].split(" - ")
        plant = info[0]
        plants_dict = reset(plants_dict, plant)

print("Plants for the exhibition:")
for k, v in plants_dict.items():
    if v[1]:
        print(f"- {k}; Rarity: {v[0]}; Rating: {(sum(v[1]) / len(v[1])):.2f}")
    else:
        print(f"- {k}; Rarity: {v[0]}; Rating: {0:.2f}")


