length = float(input()) * 100
width = float(input()) * 100
columns = length // 120
rows = (width - 100) // 70
total = columns*rows - 3
print(total)