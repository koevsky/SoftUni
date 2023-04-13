from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Eddy", "Cat", "meow")

    def test_correct_init(self):
        self.assertEqual(self.mammal.name, "Eddy")
        self.assertEqual(self.mammal.type, "Cat")
        self.assertEqual(self.mammal.sound, "meow")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        expected = "Eddy makes meow"
        self.assertEqual(self.mammal.make_sound(), expected)

    def test_get_Kingdom(self):
        expected = "animals"
        self.assertEqual(self.mammal.get_kingdom(), expected)

    def test_info(self):
        expected = "Eddy is of type Cat"
        self.assertEqual(self.mammal.info(), expected)


if __name__ == "__main__":
    main()