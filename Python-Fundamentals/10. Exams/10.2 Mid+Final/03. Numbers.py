int_seq = [int(x) for x in input().split(" ")]
average_val = sum(int_seq) / len(int_seq)
counter = 0
top_5 = []
for x in sorted(int_seq, reverse=True):
    if x > average_val:
        top_5.append(x)
        counter += 1
        if counter == 5:
            break
top_5 = sorted(top_5, reverse=True)
if top_5:
    print(*top_5)
else:
    print("No")