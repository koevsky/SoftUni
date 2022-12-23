prime_num_sum = 0
non_prime_num_sum = 0
while True:
    division_counter = 0
    data = input()
    if data == "stop":
        print(f"Sum of all prime numbers is: {prime_num_sum}")
        print(f"Sum of all non prime numbers is: {non_prime_num_sum}")
        break
    digit = int(data)
    if digit < 0:
        print("Number is negative.")
        continue
    for x in range(1, digit+1):
        if digit % x == 0:
            division_counter += 1
    if division_counter == 2:
        prime_num_sum += digit
    else:
        non_prime_num_sum += digit
