c_stack = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_counter = 1
current_rack = rack_capacity

while c_stack:
    current_num = c_stack.pop()
    if current_rack - current_num >= 0:
        current_rack -= current_num
    else:
        racks_counter += 1
        current_rack = rack_capacity - current_num

print(racks_counter)