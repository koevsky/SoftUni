text = input()
summed = 0
for i in text:
    if i == "a":
        summed += 1
    elif i == "e":
        summed += 2
    elif i == "i":
        summed += 3
    elif i == "o":
        summed += 4
    elif i == "u":
        summed += 5

print(summed)