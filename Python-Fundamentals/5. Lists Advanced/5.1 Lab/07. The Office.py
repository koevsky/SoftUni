def happiness_calc(seq, num):
    res = ""
    seq = [x * num for x in seq]
    average_value = sum(seq) / len(seq)
    satisfied_seq = list(filter(lambda x:  average_value <= x, seq))
    if len(satisfied_seq) >= len(seq)/2:
        res = f"Score: {len(satisfied_seq)}/{len(seq)}. Employees are happy!"
    else:
        res = f"Score: {len(satisfied_seq)}/{len(seq)}. Employees are not happy!"

    return res


emp_happiness = list(map(int, input().split(" ")))
factor = int(input())
print(happiness_calc(emp_happiness, factor))
