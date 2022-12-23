nums_seq = input().split(" ")
k = int(input())
result_list = []
last_index = 0
index = 0
counter = 0
while nums_seq:
    if index > len(nums_seq)-1:
       index = 0
    counter += 1
    if counter == k:
        result_list.append(nums_seq[index])
        nums_seq.pop(index)
        counter = 0
        continue
    index += 1
print(f"[{','.join(result_list)}]")
