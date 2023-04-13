from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):

    def setUp(self) -> None:

        self.movie = Movie("The X-Files", 1993, 9.8)
        self.second_movie = Movie("Mandalorian", 2019, 9.5)

    def test_correct_init(self):
        self.assertEqual(self.movie.name, "The X_Files")
        self.assertEqual(self.movie.year, 1993)
        self.assertEqual(self.movie.rating, 9.8)
        self.assertEqual(self.movie.actors, [])

    def test_empty_name_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_incorrect_year_raise_VE(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_name_not_in_list(self):

        self.movie.actors = ['Scully', 'Mulder']
        self.movie.add_actor('Skinner')

        self.assertEqual(self.movie.actors, ['Scully', 'Mulder', 'Skinner'])

    def test_name_in_list(self):
        self.movie.actors = ['Scully', 'Mulder', 'Skinner']
        message = self.movie.add_actor('Mulder')
        expected_message = "Mulder is already added in the list of actors!"
        self.assertEqual(message, expected_message)
        self.assertEqual(self.movie.actors, ['Scully', 'Mulder', 'Skinner'])

    def test_movie_rating_comparison_first_lower(self):
        self.movie.rating = 8.0
        message = self.movie.__gt__(self.second_movie)
        expected_message = '"Mandalorian" is better than "The X-Files"'

        self.assertEqual(message, expected_message)

    def test_movie_rating_comparison_second_lower(self):
        self.second_movie.rating = 8.0
        message = self.movie.__gt__(self.second_movie)
        expected_message = '"The X-Files" is better than "Mandalorian"'

        self.assertEqual(message, expected_message)

    def test_repr(self):
        self.movie.actors = ['Scully', 'Mulder', 'Skinner']

        message = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(self.movie.actors)}"

        self.assertEqual(repr(self.movie), message)




if __name__ == '__main__':
    main()


