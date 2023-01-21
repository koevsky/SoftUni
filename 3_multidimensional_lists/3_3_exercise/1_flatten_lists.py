nums_list = input().split("|")
nums_list = reversed([x.strip().split() for x in nums_list])
matrix = []
[matrix.extend(x) for x in nums_list]
print(" ".join(matrix))



