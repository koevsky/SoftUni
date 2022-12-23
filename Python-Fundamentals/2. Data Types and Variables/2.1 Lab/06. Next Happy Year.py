year = int(input())
current_year = year+1

while True:
    if current_year > year and len(set(str(current_year))) >= len(str(year)):
        print(current_year)
        break
    else:
        current_year += 1