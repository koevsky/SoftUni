n_tabs = int(input())
salary = float(input())


for n in range(n_tabs):
    tab_opened = input()
    if tab_opened == "Facebook":
        salary -= 150
    elif tab_opened == "Instagram":
        salary -= 100
    elif tab_opened == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(int(salary))