turns = int(input())

total_points = 0

zero_to_nine = 0
ten_to_nineteen = 0
twenty_to_twenty_nine = 0
thirty_to_thirty_nine = 0
forty_to_fifty = 0
invalid_numbers = 0

for x in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        zero_to_nine += 1
        total_points += number * 20/100

    elif 10 <= number <= 19:
        ten_to_nineteen += 1
        total_points += number * 30/100

    elif 20 <= number <= 29:
        twenty_to_twenty_nine += 1
        total_points += number * 40/100

    elif 30 <= number <= 39:
        thirty_to_thirty_nine += 1
        total_points += 50

    elif 40 <= number <= 50:
        forty_to_fifty += 1
        total_points += 100

    else:
        total_points /= 2
        invalid_numbers += 1

print(f"{total_points:.2f}")
print(f"From 0 to 9: {(zero_to_nine / turns * 100):.2f}%")
print(f"From 10 to 19: {(ten_to_nineteen / turns * 100):.2f}%")
print(f"From 20 to 29: {(twenty_to_twenty_nine / turns * 100):.2f}%")
print(f"From 30 to 39: {(thirty_to_thirty_nine / turns * 100):.2f}%")
print(f"From 40 to 50: {(forty_to_fifty / turns * 100):.2f}%")
print(f"Invalid numbers: {(invalid_numbers / turns * 100):.2f}%")
