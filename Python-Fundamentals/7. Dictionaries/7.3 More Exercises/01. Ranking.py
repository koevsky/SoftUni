contest_data = {}
users_data = {}
while True:
    contest_info = input()
    if contest_info == "end of contests":
        break
    contest_info = contest_info.split(":")
    contest_name, contest_password = contest_info[0], contest_info[1]
    contest_data[contest_name] = contest_password

while True:
    user_line = input()
    if user_line == "end of submissions":
        break
    user_line = user_line.split("=>")
    contest, password, username, points = user_line[0], user_line[1], user_line[2], int(user_line[3])
    if contest in contest_data.keys() and password == contest_data[contest]:
        if username not in users_data.keys():
            users_data[username] = {contest: points}
        else:
            if contest not in users_data[username].keys():
                users_data[username][contest] = points
            else:
                if points > users_data[username][contest]:
                    users_data[username][contest] = points

best_candidate = {k: sum([v[x] for x in v.keys()]) for k, v in users_data.items()}
best_candidate = sorted(best_candidate.items(), key=lambda x: x[1], reverse=True)[0]
users_data_sorted = sorted(users_data.items(), key=lambda x: x[0])
print(f"Best candidate is {best_candidate[0]} with total {best_candidate[1]} points.")
print("Ranking:")
for name, data in users_data_sorted:
    print(name)
    data_sorted = dict(sorted(dict(data).items(), key=lambda x: x[1], reverse=True))
    for k, v in data_sorted.items():
        print(f"#  {k} -> {v}")

