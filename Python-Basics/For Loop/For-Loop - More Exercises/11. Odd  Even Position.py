import sys
n = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for nums in range(1, n+1):
    digit = float(input())
    if nums % 2 == 0:
        even_sum += digit
        if digit > even_max:
            even_max = digit
        if digit < even_min:
            even_min = digit
    else:
        odd_sum += digit
        if digit > odd_max:
            odd_max = digit
        if digit < odd_min:
            odd_min = digit

print(f"OddSum={odd_sum:.2f},")
if n == 1 or n == 0:
    if odd_sum == 0:
        print("OddMin=No,")
        print("OddMax=No,")
    else:
        print(f"OddMin={odd_min:.2f},")
        print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if n == 1 or n == 0:
    if even_sum == 0:
        print("EvenMin=No,")
        print("EvenMax=No")
    else:
        print(f"EvenMin={even_min:.2f},")
        print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")











