deposit = float(input())
period = int(input())
annual_rate = float(input())
total_sum = deposit + period * ((deposit * annual_rate/100)/12)
print(total_sum)