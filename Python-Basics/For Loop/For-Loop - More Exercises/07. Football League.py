stadium_capacity = int(input())
fans_count = int(input())

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for fans in range(fans_count):
    sector_type = input()
    if sector_type == "A":
        sector_A += 1
    elif sector_type == "B":
        sector_B += 1
    elif sector_type == "V":
        sector_V += 1
    elif sector_type == "G":
        sector_G += 1

print(f"{(sector_A / fans_count * 100):.2f}%")
print(f"{(sector_B / fans_count * 100):.2f}%")
print(f"{(sector_V / fans_count * 100):.2f}%")
print(f"{(sector_G / fans_count * 100):.2f}%")
print(f"{(fans_count / stadium_capacity * 100):.2f}%")
