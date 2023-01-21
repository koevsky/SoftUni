n = int(input())
stack = []
for _ in range(n):
    line = input().split()
    if line[0] == "1":
        num = int(line[1])
        stack.append(num)
    elif line[0] == "2" and stack:
        stack.pop()
    elif line[0] == "3" and stack:
        print(max(stack))
    elif line[0] == "4" and stack:
        print(min(stack))

print(", ".join(reversed([str(x) for x in stack])))