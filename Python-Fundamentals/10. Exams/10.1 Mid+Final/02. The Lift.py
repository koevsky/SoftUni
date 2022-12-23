people_count = int(input())
lift_wagons = [int(x) for x in input().split(" ")]

for wagon in range(len(lift_wagons)):
    people_to_add = 4 - lift_wagons[wagon]
    if people_count - people_to_add >= 0:
        lift_wagons[wagon] += people_to_add
        people_count -= people_to_add
    else:
        lift_wagons[wagon] += people_count
        people_count = 0

if people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
elif people_count == 0:
    if len(lift_wagons) * "4" != "".join([str(x) for x in lift_wagons]):
        print("The lift has empty spots!")
print(*lift_wagons)