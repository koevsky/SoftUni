from collections import deque

caffeine_milligrams = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

max_caffeine = 300
total_caffeine = 0

while caffeine_milligrams and energy_drinks:

    current_caffeine_dose = caffeine_milligrams[-1] * energy_drinks[0]

    if total_caffeine + current_caffeine_dose <= max_caffeine:

        total_caffeine += current_caffeine_dose
        caffeine_milligrams.pop()
        energy_drinks.popleft()

    else:

        caffeine_milligrams.pop()
        energy_drinks.append(energy_drinks.popleft())
        total_caffeine -= 30

        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")