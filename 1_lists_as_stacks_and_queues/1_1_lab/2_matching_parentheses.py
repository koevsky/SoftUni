text = input()
p = []
for idx in range(len(text)):
    char = text[idx]
    if char == "(":
        p.append(idx)
    elif char == ")":
        print(text[p.pop(): idx+1])
