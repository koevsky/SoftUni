pencil_count = int(input())
marker_count = int(input())
detergent_liters = int(input())
discount = int(input()) / 100

total_sum = pencil_count * 5.80 + marker_count * 7.20 + detergent_liters * 1.20
discounted_sum = total_sum - (total_sum*discount)
print(discounted_sum)