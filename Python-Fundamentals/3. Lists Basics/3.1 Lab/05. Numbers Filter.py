num_list = [int(input()) for x in range(int(input()))]
nums_filtered =[]
command = input()
if command == "even":
    nums_filtered = [y for y in num_list if y % 2 == 0]
elif command == "odd":
    nums_filtered = [y for y in num_list if y % 2 != 0]
elif command == "negative":
    nums_filtered = [y for y in num_list if y < 0]
elif command == "positive":
    nums_filtered = [y for y in num_list if y >= 0]
print(nums_filtered)