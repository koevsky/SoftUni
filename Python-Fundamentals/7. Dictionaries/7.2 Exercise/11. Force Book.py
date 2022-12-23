def add_user(side, user_name, force_dict):
    force_dict = dict(force_dict)
    is_user_found = False
    for sides in force_dict.keys():
        if user_name in force_dict[sides]:
            is_user_found = True
            break
    if not is_user_found and side not in force_dict.keys():
        force_dict[side] = [user_name]
    elif not is_user_found and side in force_dict.keys():
        force_dict[side].append(user_name)

    return force_dict


def update_user(side, user_name, force_dict):
    force_dict = dict(force_dict)
    is_user_found = False
    for sides in force_dict.keys():
        if user_name in force_dict[sides]:
            is_user_found = True
            force_dict[sides].remove(user_name)
            break

    if not is_user_found and side not in force_dict.keys():
        force_dict[side] = [user_name]
    elif not is_user_found and side in force_dict.keys():
        force_dict[side].append(user_name)
    elif is_user_found:
        if side not in force_dict.keys():
            force_dict[side] = [user_name]
        else:
            force_dict[side].append(user_name)

    return force_dict, print(f"{user_name} joins the {side} side!")


def stats(force_dict):
    force_dict = dict(force_dict)
    res = ""
    for key, val in force_dict.items():
        if len(val) > 0:
            res += f"Side: {key}, Members: {len(val)}\n"
            for x in val:
                res += f"! {x}\n"

    return res


my_dict = {}
while True:
    line = input()
    if line == "Lumpawaroo":
        break
    if "|" in line:
        line = line.split(" | ")
        force_side, force_user = line[0], line[1]
        my_dict = add_user(force_side, force_user, my_dict)
    elif "->" in line:
        line = line.split(" -> ")
        force_user, force_side = line[0], line[1]
        my_dict = update_user(force_side, force_user, my_dict)[0]

print(stats(my_dict))