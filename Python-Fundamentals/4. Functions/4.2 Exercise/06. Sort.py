def srt(x):
    x = [int(n) for n in x]
    return sorted(x)

nums = input().split(" ")
print(srt(nums))
