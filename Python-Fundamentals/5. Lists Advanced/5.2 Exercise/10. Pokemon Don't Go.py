def list_manipulator(num_seq, i):
    num_seq = list(num_seq)
    i = int(i)
    removed_element_value = None
    if 0 <= i <= len(num_seq)-1:    # index in range
        removed_element_value = num_seq[i]
        num_seq.pop(i)
        for x in range(len(num_seq)):
            if num_seq[x] <= removed_element_value:
                num_seq[x] += removed_element_value
            else:
                num_seq[x] -= removed_element_value

    elif i < 0:     # Index less than 0
        removed_element_value = num_seq[0]
        num_seq.pop(0)
        num_seq.insert(0, num_seq[-1])  # Possible mistake ?
        for x in range(len(num_seq)):
            if num_seq[x] <= removed_element_value:
                num_seq[x] += removed_element_value
            else:
                num_seq[x] -= removed_element_value

    elif i > len(num_seq) - 1:  # Index bigger than range
        removed_element_value = num_seq[-1]
        num_seq.insert(-1, num_seq[0])
        num_seq.pop(-1)
        for x in range(len(num_seq)):
            if num_seq[x] <= removed_element_value:
                num_seq[x] += removed_element_value
            else:
                num_seq[x] -= removed_element_value

    return num_seq, removed_element_value


int_list = list(map(int, input().split(" ")))
result_list = []
while int_list:
    index = int(input())
    result_list.append(list_manipulator(int_list, index)[1])
    int_list = list_manipulator(int_list, index)[0]
print(sum(result_list))





