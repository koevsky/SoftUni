submissions = {}
users = {}

while True:
    line = input()
    if line == "exam finished":
        break
    line = line.split("-")
    if len(line) == 2 and line[1] == "banned":
        username = line[0]
        users.pop(username)

    elif len(line) > 2:
        username, language, points = line[0], line[1], int(line[2])
        if language not in submissions.keys():
            submissions[language] = 1
        else:
            submissions[language] += 1

        if username not in users.keys():
            users[username] = {language: points}
        else:
            if language not in users[username].keys():
                users[username][language] = points
            else:
                if points > users[username][language]:
                    users[username][language] = points
print("Results:")
for key, val in users.items():
    for languages in users[key].keys():
        print(f"{key} | {users[key][languages]}")

print("Submissions:")
for key, val in submissions.items():
    print(f"{key} - {val}")







