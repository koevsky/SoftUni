num = int(input())
is_prime = True
if num > 1:
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            break
    print(is_prime)