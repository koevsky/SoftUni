from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):

    def setUp(self) -> None:

        self.petshop = PetShop("TestName")

    def test_correct_init(self):
        self.assertEqual(self.petshop.name, "TestName")
        self.assertEqual(self.petshop.food, {})
        self.assertEqual(self.petshop.pets, [])

    def test_add_food_invalid_qty_raise_VE(self):
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}

        with self.assertRaises(ValueError) as ve:
            self.petshop.add_food("TestFood1", 0)

        self.assertEqual(str(ve.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_valid_qty(self):
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}
        result = self.petshop.add_food("TestFood1", 20)
        expected_result = "Successfully added 20.00 grams of TestFood1."
        expected_dict = {"TestFood1": 40, "TestFood2": 34}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.petshop.food, expected_dict)

    def test_add_food_new_food_name(self):
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}
        result = self.petshop.add_food("TestFood3", 100)
        expected_result = "Successfully added 100.00 grams of TestFood3."
        expected_dict = {"TestFood1": 20, "TestFood2": 34, "TestFood3": 100}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.petshop.food, expected_dict)

    def test_add_pet_already_added_raise_EXC(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3']

        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet("Name1")

        self.assertEqual(str(ex.exception), "Cannot add a pet with the same name")

    def test_add_pet(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3']
        result = self.petshop.add_pet("Name4")
        expected_result = "Successfully added Name4."
        expected_lst = ['Name1', 'Name2', 'Name3', 'Name4']

        self.assertEqual(result, expected_result)
        self.assertEqual(self.petshop.pets, expected_lst)

    def test_feed_pet_invalid_pet_name_raise_EXC(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3', 'Name4']
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}

        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet("TestFood1", "NameX")

        self.assertEqual(str(ex.exception), "Please insert a valid pet name")

    def test_feed_pet_invalid_food_name(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3', 'Name4']
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}

        result = self.petshop.feed_pet("TestFood3", "Name1")
        expected_result = f'You do not have TestFood3'

        self.assertEqual(result, expected_result)

    def test_feed_pet_insufficient_food_qty(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3', 'Name4']
        self.petshop.food = {"TestFood1": 20, "TestFood2": 34}

        result = self.petshop.feed_pet("TestFood1", "Name1")
        expected_result = "Adding food..."

        expected_dict = {"TestFood1": 1020.00, "TestFood2": 34}
        self.assertEqual(result, expected_result)
        self.assertEqual(self.petshop.food, expected_dict)

    def test_feed_pet_successfully(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3', 'Name4']
        self.petshop.food = {"TestFood1": 300, "TestFood2": 500}

        result = self.petshop.feed_pet("TestFood1", "Name1")
        expected_result = "Name1 was successfully fed"
        expected_dict = {"TestFood1": 200, "TestFood2": 500}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.petshop.food, expected_dict)

    def test_repr_override(self):
        self.petshop.pets = ['Name1', 'Name2', 'Name3', 'Name4']
        self.petshop.food = {"TestFood1": 300, "TestFood2": 500}

        expected_result = f'Shop {self.petshop.name}:\n' \
               f'Pets: {", ".join(self.petshop.pets)}'

        result = repr(self.petshop)

        self.assertEqual(result, expected_result)




if __name__ == '__main__':
    main()