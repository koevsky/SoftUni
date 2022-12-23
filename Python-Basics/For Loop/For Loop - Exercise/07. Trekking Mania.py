group_count = int(input())

musala_group = 0
mont_blanc_group = 0
kilimandjaro_group = 0
K2_group = 0
everest_group = 0

for x in range(group_count):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala_group += people_per_group
    elif 6 <= people_per_group <= 12:
        mont_blanc_group += people_per_group
    elif 13 <= people_per_group <= 25:
        kilimandjaro_group += people_per_group
    elif 26 <= people_per_group <= 40:
        K2_group += people_per_group
    elif people_per_group >= 41:
        everest_group += people_per_group

total_people = musala_group + mont_blanc_group + kilimandjaro_group + K2_group + everest_group

print(f"{(musala_group / total_people * 100):.2f}%")
print(f"{(mont_blanc_group / total_people * 100):.2f}%")
print(f"{(kilimandjaro_group / total_people * 100):.2f}%")
print(f"{(K2_group / total_people * 100):.2f}%")
print(f"{(everest_group / total_people * 100):.2f}%")