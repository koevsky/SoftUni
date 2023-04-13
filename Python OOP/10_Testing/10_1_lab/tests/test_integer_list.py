from unittest import TestCase, main


class IntegerListTest(TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList('a', 1, False, 2, 4.5, 3, ["a", 5])

    def test_correct_init(self):
        data = self.integer_list._IntegerList__data
        self.assertEqual([1, 2, 3], data)

    def test_get_data_list(self):

        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_non_int_element_to_data_list_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('m')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_integer_to_data_list_at_the_end(self):
        data = self.integer_list._IntegerList__data
        self.integer_list.add(4)
        self.assertIn(4, data)
        self.assertEqual([1, 2, 3, 4], data)

    def test_remove_invalid_index_from_data_list_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_correctly_removal_of_valid_index_from_data_list(self):

        number = self.integer_list.remove_index(2)
        data = self.integer_list._IntegerList__data

        self.assertEqual([1, 2], data)
        self.assertEqual(3, number)

    def test_get_element_with_invalid_index_from_data_list_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(3)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_with_correct_index_from_data_list(self):
        number = self.integer_list.get(0)
        self.assertEqual(1, number)

    def test_insert_element_at_invalid_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(3, 1)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_non_integer_element_at_valid_index_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 'm')

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_integer_element_at_valid_index(self):
        data = self.integer_list._IntegerList__data

        self.integer_list.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], data)

    def test_get_biggest_element_from_data_list(self):
        biggest = self.integer_list.get_biggest()
        self.assertEqual(3, biggest)

    def test_get_index_of_element_in_data_list(self):
        index = self.integer_list.get_index(1)
        self.assertEqual(0, index)


if __name__ == '__main__':
    main()