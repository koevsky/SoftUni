student, standard, kids = 0, 0, 0
while True:
    movie_name = input()
    if movie_name == "Finish":
        total = standard + student + kids
        print(f"Total tickets: {total}")
        print(f"{(student / total * 100):.2f}% student tickets.")
        print(f"{(standard / total * 100):.2f}% standard tickets.")
        print(f"{(kids / total * 100):.2f}% kids tickets.")
        break
    free_places = int(input())
    seats_taken = 0
    for p in range(free_places):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kids += 1
        seats_taken += 1
    print(f"{movie_name} - {(seats_taken / free_places * 100):.2f}% full.")
