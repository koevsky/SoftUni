from collections import deque

rows, cols = [int(x) for x in input().split()]

text = deque(list(input()))

res = []

for row in range(rows):

    current_text = ""

    for col in range(cols):
        char = text.popleft()
        current_text += char
        text.append(char)

    if row % 2 == 0:
        res.append(current_text)
    else:
        res.append(current_text[::-1])

[print(r) for r in res]