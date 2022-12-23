import sys


def exchange(index, lst):
    index = int(index)
    if 0 <= index <= len(lst)-1:
        first_half = lst[:index+1]
        second_half = lst[index+1:]
        new_lst = second_half + first_half
        return new_lst
    else:
        print("Invalid index")
        return lst


def max_even(lst):
    max_el = -sys.maxsize
    max_even_index = "" # Check
    for x in range(len(lst)):
        if int(lst[x]) % 2 == 0 and int(lst[x]) >= max_el:
            max_el = lst[x]
            max_even_index = str(x) # Check
    if max_even_index:
        return max_even_index
    else:
        return "No matches"


def max_odd(lst):
    max_el = -sys.maxsize
    max_odd_index = "" # Check
    for x in range(len(lst)):
        if int(lst[x]) % 2 != 0 and int(lst[x]) >= max_el:
            max_el = lst[x]
            max_odd_index = str(x) # Check
    if max_odd_index:
        return max_odd_index
    else:
        return "No matches"


def min_even(lst):
    min_el = sys.maxsize
    min_even_index = "" # Check
    for x in range(len(lst)):
        if int(lst[x]) % 2 == 0 and int(lst[x]) <= min_el:
            min_el = lst[x]
            min_even_index = str(x) # Check
    if min_even_index:
        return min_even_index
    else:
        return "No matches"


def min_odd(lst):
    min_el = sys.maxsize
    min_odd_index = "" # Check
    for x in range(len(lst)):
        if int(lst[x]) % 2 != 0 and int(lst[x]) <= min_el:
            min_el = lst[x]
            min_odd_index = str(x) # Check
    if min_odd_index:
        return min_odd_index
    else:
        return "No matches"


def first_even(num, lst):
    num = int(num)
    first_even_lst = []
    if 0 < num <= len(lst):
        counter = 0
        for x in lst:
            if counter == num:
                break
            if int(x) % 2 == 0:
                first_even_lst.append(x)
                counter += 1
        return first_even_lst
    else:
        return "Invalid count"


def first_odd(num, lst):
    num = int(num)
    first_odd_lst = []
    if 0 < num <= len(lst):
        counter = 0
        for x in lst:
            if counter == num:
                break
            if int(x) % 2 != 0:
                first_odd_lst.append(x)
                counter += 1
        return first_odd_lst
    else:
        return "Invalid count"


def last_even(num, lst):
    num = int(num)
    rev_lst = list(reversed(lst))
    last_even_lst = []
    if 0 < num <= len(lst):
        counter = 0
        for x in rev_lst:
            if counter == num:
                break
            if int(x) % 2 == 0:
                last_even_lst.append(x)
                counter += 1
        return list(reversed(last_even_lst))
    else:
        return "Invalid count"


def last_odd(num, lst):
    num = int(num)
    rev_lst = list(reversed(lst))
    last_odd_lst = []
    if 0 < num <= len(lst):
        counter = 0
        for x in rev_lst:
            if counter == num:
                break
            if int(x) % 2 != 0:
                last_odd_lst.append(x)
                counter += 1
        return list(reversed(last_odd_lst))
    else:
        return "Invalid count"


nums_list = input().split(" ")
nums_list = [int(n) for n in nums_list]
while True:
    line = input()
    if line == "end":
        break
    line = line.split(" ")
    if line[0] == "exchange":
        idx = int(line[1])
        nums_list = exchange(idx, nums_list)
    elif line[0] == "max":
        if line[1] == "even":
            print(max_even(nums_list))
        elif line[1] == "odd":
            print(max_odd(nums_list))
    elif line[0] == "min":
        if line[1] == "even":
            print(min_even(nums_list))
        elif line[1] == "odd":
            print(min_odd(nums_list))
    elif line[0] == "first":
        count = int(line[1])
        if line[2] == "even":
            print(first_even(count, nums_list))
        elif line[2] == "odd":
            print(first_odd(count, nums_list))
    elif line[0] == "last":
        count = int(line[1])
        if line[2] == "even":
            print(last_even(count, nums_list))
        elif line[2] == "odd":
            print(last_odd(count, nums_list))
print(nums_list)