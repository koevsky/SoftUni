def palindrome_checker(x):
        if x == x[::-1]:
            return True
        return False

nums = input().split(", ")
for i in nums:
    print(palindrome_checker(i))