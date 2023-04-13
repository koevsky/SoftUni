from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):

    def setUp(self) -> None:
        self.cart_one = ShoppingCart("NameOne", 200)
        self.cart_two = ShoppingCart("NameTwo", 300)

    def test_correct_init(self):
        self.assertEqual(self.cart_one.shop_name, "NameOne")
        self.assertEqual(self.cart_one.budget, 200)
        self.assertEqual(self.cart_one.products, {})

    def test_invalid_shop_name_no_upper_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.cart_one.shop_name = "nameOne"

        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_invalid_shop_name_num_in_name_raise_ValueError(self):
        with self.assertRaises(ValueError) as ve:
            self.cart_one.shop_name = "Name1"

        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_invalid_product_price_raise_ValueError(self):
        product_name = "Glue"

        with self.assertRaises(ValueError) as ve:
            self.cart_one.add_to_cart(product_name, 100)

        self.assertEqual(str(ve.exception), f"Product {product_name} cost too much!")

    def test_add_to_cart_successfully(self):
        self.cart_one.products = {"tools": 20, "glue": 50}

        product_name = "paint"
        expected_result = f"{product_name} product was successfully added to the cart!"
        result = self.cart_one.add_to_cart(product_name, 40)

        expected_dict = {"tools": 20, "glue": 50, "paint": 40}
        self.assertEqual(result, expected_result)
        self.assertEqual(self.cart_one.products, expected_dict)

    def test_remove_from_cart_invalid_product_name_raise_ValueError(self):
        self.cart_one.products = {"tools": 20, "glue": 50, "paint": 40}
        product_name = "brush"
        with self.assertRaises(ValueError) as ve:
            self.cart_one.remove_from_cart(product_name)

        self.assertEqual(str(ve.exception), f"No product with name {product_name} in the cart!")

    def test_remove_from_cart_valid_item_name(self):
        self.cart_one.products = {"tools": 20, "glue": 50, "paint": 40}
        product_name = "tools"
        result = self.cart_one.remove_from_cart(product_name)
        expected_result = f"Product {product_name} was successfully removed from the cart!"

        expected_dict = {"glue": 50, "paint": 40}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.cart_one.products,expected_dict)

    def test_add_two_instances(self):
        self.cart_one.products = {"tools": 20, "glue": 50, "paint": 40}
        self.cart_two.products = {"saw": 10, "wood": 20}

        expected_budget = 500
        expected_name = "NameOneNameTwo"
        expected_products = {"tools": 20, "glue": 50, "paint": 40, "saw": 10, "wood": 20}

        result = self.cart_one.__add__(self.cart_two)
        self.assertTrue(isinstance(result, ShoppingCart))
        self.assertEqual(result.budget, expected_budget)
        self.assertEqual(result.shop_name, expected_name)
        self.assertEqual(result.products, expected_products)

    def test_buy_products_insufficient_budget_raise_ValueError(self):
        self.cart_one.budget = 100
        self.cart_one.products = {"tools": 20, "glue": 50, "paint": 40, "saw": 10, "wood": 20}

        money_value = sum(self.cart_one.products.values()) - self.cart_one.budget

        with self.assertRaises(ValueError) as ve:
            self.cart_one.buy_products()

        self.assertEqual(str(ve.exception), f"Not enough money to buy the products! Over budget with {money_value:.2f}lv!")

    def test_buy_products_successfully(self):
        self.cart_one.budget = 200
        self.cart_one.products = {"tools": 20, "glue": 50, "paint": 40, "saw": 10, "wood": 20}
        total_sum = sum(self.cart_one.products.values())

        result = self.cart_one.buy_products()
        expected_result = f'Products were successfully bought! Total cost: {total_sum:.2f}lv.'
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()