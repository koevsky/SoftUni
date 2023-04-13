from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):

    def setUp(self) -> None:

        self.library = Library("TestName")

    def test_correct_init(self):

        self.assertEqual(self.library.name, "TestName")
        self.assertEqual(self.library.books_by_authors, {})
        self.assertEqual(self.library.readers, {})

    def test_empty_name_string_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual(str(ve.exception), "Name cannot be empty string!")

    def test_add_book_new_author_added(self):
        self.library.books_by_authors = {"a": ["ab", "cd"]}
        self.library.add_book("b", "bc")

        expected_dict = {"a": ["ab", "cd"], "b": ["bc"]}

        self.assertEqual(self.library.books_by_authors, expected_dict)
        self.assertDictEqual(self.library.books_by_authors, expected_dict)

    def test_add_book_author_already_added(self):
        self.library.books_by_authors = {"a": ["ab", "cd"], "b": ["bc"]}
        self.library.add_book("b", "cm")

        expected_dict = {"a": ["ab", "cd"], "b": ["bc", "cm"]}

        self.assertEqual(self.library.books_by_authors, expected_dict)

    def test_add_reader_new_reader(self):
        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        self.library.add_reader("Tn3")

        expected_dict = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}], "Tn3": []}

        self.assertEqual(self.library.readers, expected_dict)

    def test_add_reader_already_added(self):
        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        message = self.library.add_reader("Tn2")
        expected_message = f"Tn2 is already registered in the {self.library.name} library."
        expected_dict = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}

        self.assertEqual(message, expected_message)
        self.assertEqual(self.library.readers, expected_dict)

    def test_rent_book_not_valid_reader_name(self):

        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        self.library.books_by_authors = {"a": ["ab", "cd"], "b": ["bc"]}

        message = self.library.rent_book("Tn3", "a", "ab")
        expected_message = f"Tn3 is not registered in the {self.library.name} Library."

        self.assertEqual(message, expected_message)

    def test_rent_book_invalid_book_author(self):

        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        self.library.books_by_authors = {"a": ["ab", "cd"], "b": ["bc"]}

        message = self.library.rent_book("Tn1", "c", "nh")
        expected_message = f"{self.library.name} Library does not have any c's books."

        self.assertEqual(message, expected_message)

    def test_rent_book_invalid_book_title(self):
        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        self.library.books_by_authors = {"a": ["ab", "cd"], "b": ["bc"]}

        message = self.library.rent_book("Tn1", "a", "nh")
        expected_message = f"""{self.library.name} Library does not have a's "nh"."""

        self.assertEqual(message, expected_message)

    def test_rent_book_valid_data_input(self):
        self.library.readers = {"Tn1": [{"a": "b"}, {"c": "d"}], "Tn2": [{"y": "x"}, {"z": "m"}]}
        self.library.books_by_authors = {"a": ["ab", "cd"], "b": ["bc"]}

        self.library.rent_book("Tn1", "a", "cd")

        expected_book_dict = {"a": ["ab"], "b": ["bc"]}
        expected_readers_dict = {"Tn1": [{"a": "b"}, {"c": "d"}, {"a": "cd"}], "Tn2": [{"y": "x"}, {"z": "m"}]}

        self.assertEqual(self.library.readers, expected_readers_dict)
        self.assertEqual(self.library.books_by_authors, expected_book_dict)







if __name__ == "__main__":
    main()