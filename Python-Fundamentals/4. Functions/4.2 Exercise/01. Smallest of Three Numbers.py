def smallest(n1, n2, n3):
    x = sorted([n1, n2, n3])
    return x[0]

num_1, num_2, num_3 = int(input()), int(input()), int(input())

print(smallest(num_1, num_2, num_3))
