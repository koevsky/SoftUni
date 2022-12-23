def pass_validator(string):
    string = str(string)
    digit_count = [1 for x in string if x.isdigit()].count(1)
    if not string.isalnum():
        print("Password must consist only of letters and digits")
    if not 6 <= len(string) <= 10:
        print("Password must be between 6 and 10 characters")
    if not digit_count >= 2:
        print("Password must have at least 2 digits")
    if string.isalnum() and 6 <= len(string) <= 10 and digit_count >= 2:
        print("Password is valid")

password = input()
pass_validator(password)