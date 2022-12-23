import math
days = int(input())
planned_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

food_eaten = days * (dog_food_per_day + cat_food_per_day + turtle_food_per_day)

if food_eaten <= planned_food:
    food_left = planned_food - food_eaten
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    food_needed = food_eaten - planned_food
    print(f"{math.ceil(food_needed)} more kilos of food are needed.")
