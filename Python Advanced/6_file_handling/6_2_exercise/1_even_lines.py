repl = ("-", ",", ".", "!", "?")

with open('text.txt', 'r') as file:

    data = file.readlines()
    data = [data[x].rstrip() for x in range(len(data)) if x % 2 == 0]

    for i in range(len(data)):
        for char in repl:
            data[i] = data[i].replace(char, "@")

        data[i] = list(reversed(data[i].split()))
        data[i] = " ".join(data[i])


[print(r) for r in data]