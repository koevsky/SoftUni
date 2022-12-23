def distribute(num_list, min_wealth):
    for i in range(len(num_list)):
        if num_list[i] < min_wealth:
            c = min_wealth - num_list[i]
            max_num = max(num_list)
            if max_num - c >= min_wealth:
                num_list[num_list.index(max_num)] -= c
                num_list[i] += c
    if sum(num_list) >= len(num_list) * min_wealth:
        return num_list
    else:
        return "No equal distribution possible"


list_of_nums = list(map(int, input().split(", ")))
minimal_wealth = int(input())
print(f"{distribute(list_of_nums, minimal_wealth)}")



