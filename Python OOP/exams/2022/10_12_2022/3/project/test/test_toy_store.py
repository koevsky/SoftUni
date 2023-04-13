from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_correct_init(self):

        expected_dict = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(self.toy_store.toy_shelf, expected_dict)

    def test_add_toy_invalid_shelf_name_raise_Exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("M", "truck")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_add_toy_already_added_raise_Exception(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("C", "truck")

        self.assertEqual(str(ex.exception), "Toy is already in shelf!")

    def test_add_toy_on_taken_shelf_raise_Exception(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("C", "statue")

        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_successfully(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "truck",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.toy_store.add_toy("D", "plane")
        expected_result = f"Toy:plane placed successfully!"
        expected_dict = {
            "A": None,
            "B": None,
            "C": "truck",
            "D": "plane",
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf, expected_dict)

    def test_remove_toy_invalid_shelf_name_raise_Exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("M", "truck")

        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_remove_toy_invalid_toy_name_raise_Exception(self):
        self.toy_store.toy_shelf = {
            "A": None,
            "B": None,
            "C": "truck",
            "D": "plane",
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("D", "doll")

        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.toy_store.toy_shelf = {
            "A": "doll",
            "B": "car",
            "C": "truck",
            "D": "plane",
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.toy_store.remove_toy("B", "car")
        expected_result = "Remove toy:car successfully!"
        expected_dict = {
            "A": "doll",
            "B": None,
            "C": "truck",
            "D": "plane",
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(result, expected_result)
        self.assertEqual(self.toy_store.toy_shelf, expected_dict)


if __name__ == "__main__":
    main()
