pool_volume = int(input())
p1 = int(input())
p2 = int(input())
time_h = float(input())

p1_volume = p1 * time_h
p2_volume = p2 * time_h
total_volume = p1_volume + p2_volume

if total_volume <= pool_volume:
    total_percentage = (p1_volume / pool_volume * 100) + (p2_volume / pool_volume * 100)
    pipe_1_percentage = p1_volume / total_volume * 100
    pipe_2_percentage = p2_volume / total_volume * 100
    print(f"The pool is {total_percentage:.2f}% full. Pipe 1: {pipe_1_percentage:.2f}%. Pipe 2: {pipe_2_percentage:.2f}%.")
else:
    liters_more = total_volume - pool_volume
    print(f"For {time_h} hours the pool overflows with {liters_more:.2f} liters.")


