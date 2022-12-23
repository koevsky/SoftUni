n = int(input())
word = input()
unfiltered = [input() for x in range(n)]
filtered = [y for y in unfiltered if word in y]
print(f"{unfiltered}\n{filtered}")