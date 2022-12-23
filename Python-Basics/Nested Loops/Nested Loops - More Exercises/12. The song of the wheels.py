control_value = int(input())
counter, password = 0, ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a*b + c*d == control_value:
                    print(f"{a}{b}{c}{d}",end=" ")
                    counter += 1
                    if counter == 4:
                        password = str(a) + str(b) + str(c) + str(d)
print()
if password:
    print(f"Password: {password}")
else:
    print("No!")

