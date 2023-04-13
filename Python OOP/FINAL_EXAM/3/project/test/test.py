from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TennisPlayerTests(TestCase):

    def setUp(self) -> None:

        self.player_one = TennisPlayer("TestNameOne", 18, 50)
        self.player_two = TennisPlayer("TestNameTwo", 19, 60)

        self.player_three = TennisPlayer("TNT", 20, 70)

    def test_correct_init(self):
        self.assertEqual(self.player_one.name, "TestNameOne")
        self.assertEqual(self.player_one.age, 18)
        self.assertEqual(self.player_one.points, 50)

        self.assertEqual(self.player_three.name, "TNT")

    def test_invalid_name_length_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.player_one.name = "TN"

        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_invalid_age_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.player_one.age = 17

        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_not_present(self):
        self.player_one.wins = ["abc", "abv", "Test123"]

        self.player_one.add_new_win("Test321")

        self.assertEqual(self.player_one.wins, ["abc", "abv", "Test123", "Test321"])
        self.assertIn("Test321", self.player_one.wins)

    def test_add_new_win_win_present_returns_message(self):

        self.player_one.wins = ["abc", "abv", "Test123"]
        message = self.player_one.add_new_win("Test123")
        expected_message = "Test123 has been already added to the list of wins!"

        self.assertEqual(message, expected_message)
        self.assertEqual(self.player_one.wins, ["abc", "abv", "Test123"])

    def test_magic_lt_current_player_best(self):
        self.player_one.points = 70

        message = self.player_one < self.player_two
        expected_message = f'TestNameOne is a better player than TestNameTwo'

        self.assertEqual(message, expected_message)

    def test_magic_lt_other_player_best(self):
        message = self.player_one < self.player_two
        expected_message = 'TestNameTwo is a top seeded player and he/she is better than TestNameOne'

        self.assertEqual(message, expected_message)

    def test_magic_lt_equal_results(self):
        self.player_one.points = 60

        message = self.player_one < self.player_two
        expected_message = 'TestNameOne is a better player than TestNameTwo'

        self.assertEqual(message, expected_message)

    def test_magic_str(self):
        self.player_one.wins = ["abc", "abv", "Test123"]

        expected_message = f"Tennis Player: {self.player_one.name}\n" \
               f"Age: {self.player_one.age}\n" \
               f"Points: {self.player_one.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player_one.wins)}"

        self.assertEqual(str(self.player_one), expected_message)


if __name__ == "__main__":
    main()

