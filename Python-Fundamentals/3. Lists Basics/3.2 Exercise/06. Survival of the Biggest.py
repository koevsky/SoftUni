numbers = input().split(" ")
numbers = [int(x) for x in numbers]
sorted_numbers = sorted(numbers)
n_count = int(input())
for n in range(n_count):
    numbers.remove(sorted_numbers[n])
numbers = [str(y) for y in numbers]
print(", ".join(numbers))