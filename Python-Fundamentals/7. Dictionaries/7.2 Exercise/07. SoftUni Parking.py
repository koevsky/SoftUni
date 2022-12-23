def register(text, parking_dict):
    parking_dict = dict(parking_dict)
    text = str(text).split(" ")
    username, plate_number = text[1], text[2]
    res = ""
    if username not in parking_dict.keys():
        parking_dict[username] = plate_number
        res = f"{username} registered {plate_number} successfully"
    else:
        res = f"ERROR: already registered with plate number {parking_dict[username]}"

    return parking_dict, print(res)


def unregister(text, parking_dict):
    parking_dict = dict(parking_dict)
    text = str(text).split(" ")
    username = text[1]
    res = ""
    if username not in parking_dict.keys():
        res = f"ERROR: user {username} not found"
    else:
        res = f"{username} unregistered successfully"
        parking_dict.pop(username)

    return parking_dict, print(res)


def parking_stats(parking_dict):
    parking_dict = dict(parking_dict)
    res = ""
    for k, v in parking_dict.items():
        res += f"{k} => {v}\n"

    return res


n = int(input())
parking = {}
for _ in range(n):
    line = input()
    if "register" == line.split(" ")[0]:
        parking = register(line, parking)[0]

    elif "unregister" == line.split(" ")[0]:
        parking = unregister(line, parking)[0]


print(parking_stats(parking))

