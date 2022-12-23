line = input()
emoticons = [line[x]+line[x+1] for x in range(len(line)) if line[x] == ":"]
for x in emoticons:
    print(x)


