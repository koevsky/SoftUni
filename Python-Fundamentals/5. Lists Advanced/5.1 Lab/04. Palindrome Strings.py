def palindromes(seq):
    pal = [x for x in seq if x == x[::-1]]
    return pal


text = input().split(" ")
word = input()
print(palindromes(text))
print(f"Found palindrome {palindromes(text).count(word)} times")