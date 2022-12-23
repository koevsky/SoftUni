contest_data = {}
user_data = {}
while True:
    line = input()
    if line == "no more time":
        break
    line = line.split(" -> ")
    username, contest, points = line[0], line[1], int(line[2])
    if contest not in contest_data.keys():
        contest_data[contest] = [username]
    else:
        if username not in contest_data[contest]:
            contest_data[contest].append(username)

    if username not in user_data.keys():
        user_data[username] = {contest: points}
    else:
        if contest not in user_data[username].keys():
            user_data[username][contest] = points
        else:
            if points > user_data[username][contest]:
                user_data[username][contest] = points


for con, name_list in contest_data.items():
    counter = 1
    print(f"{con}: {len(name_list)} participants")
    participants_points = {name: user_data[name][con] for name in name_list}
    participants_points_sorted = dict(sorted(participants_points.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for n, p in participants_points_sorted.items():
        print(f"{counter}. {n} <::> {p}")
        counter += 1

total_points = {key: sum([val[x] for x in val.keys()]) for key, val in user_data.items()}
total_points_sorted = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
counter = 1
print("Individual standings:")
for k, v in total_points_sorted.items():
    print(f"{counter}. {k} -> {v}")
    counter += 1
