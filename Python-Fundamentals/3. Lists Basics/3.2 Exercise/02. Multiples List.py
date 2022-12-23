factor, count = int(input()), int(input())
new_list = [x for x in range(1, (count+1) * factor) if x % factor == 0]
print(new_list)