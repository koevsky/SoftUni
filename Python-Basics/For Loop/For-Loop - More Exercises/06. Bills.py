period = int(input())

total_electricity_bill = 0
total_water_bill = 0
total_internet_bill = 0
total_other_bill = 0

average_bill = 0

for x in range(period):
    electricity_bill =  float(input())
    total_electricity_bill += electricity_bill
    total_water_bill += 20
    total_internet_bill += 15
    total_other_bill += 20 + 15 + electricity_bill + (20 + 15 + electricity_bill) * 20/100

average_bill = (total_electricity_bill + total_water_bill + total_internet_bill + total_other_bill) / period

print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_other_bill:.2f} lv")
print(f"Average: {average_bill:.2f} lv")