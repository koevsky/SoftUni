ticket_counter = 0
student_tickets, standard_tickets, kids_tickets = 0, 0, 0
while True:
    movie_name = input()
    if movie_name == "Finish":
        print(f"Total tickets: {ticket_counter}")
        print(f"{(student_tickets / ticket_counter * 100):.2f}% student tickets.")
        print(f"{(standard_tickets / ticket_counter * 100):.2f}% standard tickets.")
        print(f"{(kids_tickets / ticket_counter * 100):.2f}% kids tickets.")
        break
    free_places = int(input())
    places_taken = 0
    for places in range(free_places):
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1
        ticket_counter += 1
        places_taken += 1
    print(f"{movie_name} - {(places_taken / free_places * 100):.2f}% full.")