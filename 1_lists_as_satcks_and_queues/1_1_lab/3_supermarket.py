from collections import deque

q = deque([])

while True:
    line = input()
    if line == "Paid":
        while q:
            print(q.popleft())

    elif line == "End":
        print(f"{len(q)} people remaining.")
        break
    else:
        q.append(line)
