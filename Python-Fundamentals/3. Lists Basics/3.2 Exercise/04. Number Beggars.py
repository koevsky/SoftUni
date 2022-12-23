numbers = input().split(", ")
beggars_count = int(input())
beggars_list = list("0"*beggars_count)
beggars_list = [int(x) for x in beggars_list]
numbers = [int(y) for y in numbers]
turns = 0
while numbers:
    beggars_list[turns] += numbers[0]
    numbers.remove(numbers[0])
    turns += 1
    if turns >= beggars_count:
        turns = 0
print(beggars_list)