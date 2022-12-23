men_tickets, women_tickets, tales_available = int(input()), int(input()), int(input())
table_counter = 0
for men in range(1, men_tickets+1):
    for women in range(1, women_tickets+1):
        table_counter += 1
        if table_counter <= tales_available:
            print(f"({men} <-> {women})", end=" ")
        else:
            break