book_searched = input()
searched_count = 0

while True:
    book_name = input()
    if book_name == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {searched_count} books.")
        break
    if book_searched == book_name:
        print(f"You checked {searched_count} books and found it.")
        break
    searched_count += 1