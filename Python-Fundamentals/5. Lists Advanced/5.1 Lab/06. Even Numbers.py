def find_even_index(seq):
    indexes = [x for x in range(len(seq)) if seq[x] % 2 == 0]
    return indexes


nums = list(map(int, input().split(",")))
print(find_even_index(nums))