def perfect_num(num):
    if num > 0:
        divisors_sum = sum([x for x in range(1, num) if num % x == 0])
        if divisors_sum == num:
            return "We have a perfect number!"

    return "It's not so perfect."

x = int(input())
print(perfect_num(x))