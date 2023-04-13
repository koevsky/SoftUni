from project.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class PaintFactoryTests(TestCase):

    def setUp(self) -> None:
        self.paint_factory = PaintFactory("TestName", 100)

    def test_correct_init(self):

        valid_ingredients = ["white", "yellow", "blue", "green", "red"]

        self.assertEqual(self.paint_factory.name, "TestName")
        self.assertEqual(self.paint_factory.capacity, 100)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, valid_ingredients)

    def test_add_invalid_ingredient_name_raise_TypeError(self):

        product_type = 'orange'
        message = f"Ingredient of type {product_type} not allowed in {self.paint_factory.__class__.__name__}"

        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient(product_type, 10)

        self.assertEqual(str(te.exception), message)

    def test_can_add_return_True(self):

        self.paint_factory.ingredients = {"blue": 30, 'red': 20}
        result = self.paint_factory.can_add(50)
        self.assertEqual(result, True)

    def test_can_add_return_False(self):

        self.paint_factory.ingredients = {"blue": 30, 'red': 20}
        result = self.paint_factory.can_add(60)
        self.assertEqual(result, False)

    def test_add_value_not_enough_space_raise_ValueError(self):

        self.paint_factory.ingredients = {"blue": 30, 'red': 20}

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("green", 60)

        self.assertEqual(str(ve.exception), "Not enough space in factory")

    def test_add_ingredient_successfully_ingredient_not_present(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20}
        self.paint_factory.add_ingredient("green", 20)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 30, 'red': 20, 'green': 20})

    def test_add_ingredient_successfully_ingredient_present(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20, "green": 20}
        self.paint_factory.add_ingredient("red", 10)
        self.assertEqual(self.paint_factory.ingredients, {"blue": 30, 'red': 30, "green": 20})

    def test_remove_ingredient_raise_KeyError(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20, 'green': 20}

        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("white", 20)

        self.assertEqual(str(ke.exception), "'No such ingredient in the factory'") #

    def test_remove_ingredient_raise_ValueError(self):

        self.paint_factory.ingredients = {"blue": 30, 'red': 20, 'green': 20}

        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("red", 30)

        self.assertEqual(str(ve.exception), "Ingredients quantity cannot be less than zero")

    def test_remove_ingredient_valid_input(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20, 'green': 20}
        self.paint_factory.remove_ingredient("red", 10)

        self.assertEqual(self.paint_factory.ingredients, {"blue": 30, 'red': 10, 'green': 20})

    def test_products_property(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20, 'green': 20}

        products = self.paint_factory.products

        self.assertEqual(self.paint_factory.ingredients, products)

    def test_repr(self):
        self.paint_factory.ingredients = {"blue": 30, 'red': 20, 'green': 20}

        result = ""
        result += f"Factory name: {self.paint_factory.name} with capacity {self.paint_factory.capacity}.\n"
        for ingredient in self.paint_factory.ingredients:
            result += f"{ingredient}: {self.paint_factory.ingredients[ingredient]}\n"

        self.assertEqual(repr(self.paint_factory), result)


if __name__ == "__main__":
    main()