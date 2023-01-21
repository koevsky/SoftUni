n = int(input())

odd_set = set()
even_set = set()

for row in range(1, n+1):
    name = input()
    name_value = sum([ord(c) for c in name]) // row
    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(odd_set) == sum(even_set):
    union = odd_set.union(even_set)
    print(", ".join([str(i) for i in union]))
elif sum(odd_set) > sum(even_set):
    difference = odd_set.difference(even_set)
    print(", ".join([str(i) for i in difference]))
elif sum(odd_set) < sum(even_set):
    s_difference = odd_set.symmetric_difference(even_set)
    print(", ".join([str(i) for i in s_difference]))
