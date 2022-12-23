def even_odd_calc(num):
    even = sum([int(x) for x in num if int(x) % 2 == 0])
    odd = sum([int(y) for y in num if int(y) % 2 != 0])
    return even, odd
x = input()
print(f"Odd sum = {even_odd_calc(x)[1]}, Even sum = {even_odd_calc(x)[0]}")