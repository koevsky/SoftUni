class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            book = next(filter(lambda b: b.title == title, self.books))

        except StopIteration:
            raise ValueError(f"There is no book with title: {title}")

        return f"Book {title} with author {book.author},  is found "





