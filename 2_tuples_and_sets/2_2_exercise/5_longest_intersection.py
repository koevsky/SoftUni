n = int(input())
longest = []

for _ in range(n):
    num_range = input().split("-")
    first_start, first_end = tuple(map(int, num_range[0].split(",")))
    second_start, second_end = tuple(map(int, num_range[1].split(",")))
    first_set = set([x for x in range(first_start, first_end+1)])
    second_set = set([y for y in range(second_start, second_end+1)])
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = list(intersection)

print(f"Longest intersection is {longest} with length {len(longest)}")