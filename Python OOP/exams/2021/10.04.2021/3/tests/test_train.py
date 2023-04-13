from project.train.train import Train
from unittest import TestCase, main


class TrainTests(TestCase):

    def setUp(self) -> None:

        self.train = Train("TestName", 200)

    def test_correct_init(self):
        self.assertEqual(self.train.name, "TestName")
        self.assertEqual(self.train.capacity, 200)
        self.assertEqual(self.train.passengers, [])

    def test_add_full_capacity_raise_VE(self):
        self.train.capacity = 5
        self.train.passengers = ["a", "b", "c", "d", "e"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("f")

        self.assertEqual(str(ve.exception), "Train is full")

    def test_add_passenger_who_is_added_raise_VE(self):
        self.train.passengers = ["a", "b", "c", "d", "e"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("a")

        self.assertEqual(str(ve.exception), "Passenger a Exists")

    def test_add_passenger_successfully(self):
        self.train.passengers = ["a", "b", "c", "d", "e"]

        message = self.train.add("g")
        expected_message = "Added passenger g"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.train.passengers, ["a", "b", "c", "d", "e", "g"])

    def test_remove_invalid_passenger_name_raise_VE(self):
        self.train.passengers = ["a", "b", "c", "d", "e"]

        with self.assertRaises(ValueError) as ve:
            self.train.remove("f")

        self.assertEqual(str(ve.exception), "Passenger Not Found")

    def test_remove_passenger_successfully(self):
        self.train.passengers = ["a", "b", "c", "d", "e"]

        message = self.train.remove("e")
        expected_message = "Removed e"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.train.passengers, ["a", "b", "c", "d"])

if __name__ == "__main__":
    main()

