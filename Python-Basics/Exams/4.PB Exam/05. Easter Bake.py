import sys, math
easter_bread = int(input())
flour_qty, sugar_qty = 0, 0
max_flour, max_sugar = -sys.maxsize, -sys.maxsize

for x in range(easter_bread):
    sugar, flour = int(input()), int(input())
    flour_qty += flour
    sugar_qty += sugar
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
print(f"Sugar: {math.ceil(sugar_qty / 950)}")
print(f"Flour: {math.ceil(flour_qty / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")


