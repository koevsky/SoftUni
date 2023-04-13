from project.bookstore import Bookstore
from unittest import TestCase, main


class BookstoreTests(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(50)

    def test_correct_init(self):
        self.assertEqual(self.bookstore.books_limit, 50)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, {})
        self.assertEqual(self.bookstore._Bookstore__total_sold_books, 0)

    def test_total_sold_books_property(self):
        self.bookstore._Bookstore__total_sold_books = 10
        self.assertEqual(self.bookstore.total_sold_books, 10)

    def test_input_zero_books_limit_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual(str(ve.exception), f"Books limit of 0 is not valid")

    def test_dunder_len(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 4, "b": 5, "c": 1, "d": 5}
        expected_result = 15

        self.assertEqual(len(self.bookstore), expected_result)

    def test_receive_book_books_over_limit_rase_Exception(self):

        self.bookstore.books_limit = 20
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1}

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("c", 4)

        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_book_already_present(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1}
        result = self.bookstore.receive_book("b", 10)
        expected_result = f"13 copies of b are available in the bookstore."
        expected_dict = {"a": 14, "b": 13, "c": 1}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_dict)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["b"], 13)

    def test_receive_book_not_present(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1}
        result = self.bookstore.receive_book("d", 10)
        expected_result = f"10 copies of d are available in the bookstore."
        expected_dict = {"a": 14, "b": 3, "c": 1, "d": 10}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_dict)
        self.assertIn("d", self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_invalid_title_raise_Exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1, "d": 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("m", 5)

        self.assertEqual(str(ex.exception), "Book m doesn't exist!")

    def test_sell_book_valid_title_invalid_count_raise_Exception(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1, "d": 10}

        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("c", 2)

        self.assertEqual(str(ex.exception), "c has not enough copies to sell. Left: 1")

    def test_sell_book_successfully(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1, "d": 10}

        result = self.bookstore.sell_book("a", 4)
        expected_result = "Sold 4 copies of a"

        expected_dict = {"a": 10, "b": 3, "c": 1, "d": 10}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_dict)
        self.assertEqual(self.bookstore.total_sold_books, 4)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["a"], 10)

    def test_sell_book_all_qty(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1, "d": 10}

        result = self.bookstore.sell_book("a", 14)
        expected_result = "Sold 14 copies of a"
        expected_dict = {"a": 0, "b": 3, "c": 1, "d": 10}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles, expected_dict)
        self.assertEqual(self.bookstore.total_sold_books, 14)
        self.assertEqual(self.bookstore.availability_in_store_by_book_titles["a"], 0)

    def test_dunder_str(self):
        self.bookstore.availability_in_store_by_book_titles = {"a": 14, "b": 3, "c": 1, "d": 10}
        self.bookstore.sell_book("a", 5)

        result = [f"Total sold books: {self.bookstore.total_sold_books}"]
        result.append(f'Current availability: {len(self.bookstore)}')
        for book_title, number_of_copies in self.bookstore.availability_in_store_by_book_titles.items():
            result.append(f" - {book_title}: {number_of_copies} copies")

        expected_result = '\n'.join(result)

        self.assertEqual(str(self.bookstore), expected_result)


if __name__ == "__main__":
    main()

