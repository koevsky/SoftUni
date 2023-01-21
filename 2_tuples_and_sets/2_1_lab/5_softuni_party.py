n = int(input())
guest_list = set(input() for _ in range(n))
arrived = set()

while True:
    line = input()
    if line == "END":
        break
    arrived.add(line)

missing = guest_list.difference(arrived)
print(len(missing))
print("\n".join(sorted(missing)))



