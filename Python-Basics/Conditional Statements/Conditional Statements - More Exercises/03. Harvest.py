import math
sq_m_field = int(input())
grapes_per_sq_m = float(input())
wine_requested = int(input())
workers_count = int(input())

total_grapes_harvested_kg = sq_m_field * grapes_per_sq_m
grapes_for_wine = total_grapes_harvested_kg * 40/100
liters_wine = grapes_for_wine / 2.5

if liters_wine < wine_requested:
    wine_needed = wine_requested - liters_wine
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")
else:
    wine_left = liters_wine - wine_requested
    wine_per_worker = wine_left / workers_count
    print(f"Good harvest this year! Total wine: {math.floor(liters_wine)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.")