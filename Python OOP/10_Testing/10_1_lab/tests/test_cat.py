from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat('Josh')

    def test_correct_init(self):
        self.assertEqual('Josh', self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_is_already_fed_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_is_sleepy_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)

    def test_cat_is_growing_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_sleep_hungry_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_sleepy_after_sleep(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()