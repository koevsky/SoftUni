initial_deck = input().split(" ")
swaps = int(input())
swap_counter = 0
while swap_counter < swaps:
    left_part = initial_deck[0:int(len(initial_deck) / 2)]
    right_part = initial_deck[int(len(initial_deck) / 2):]
    left_part.pop(0)
    right_part.pop(-1)
    faro_list = [initial_deck[0]]
    for x in range(len(left_part)):
        faro_list.append(right_part[x])
        faro_list.append(left_part[x])
    faro_list.append(initial_deck[-1])
    initial_deck = faro_list
    swap_counter += 1
print(initial_deck)