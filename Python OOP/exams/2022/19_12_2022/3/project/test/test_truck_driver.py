from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("TestName", 1)

    def test_correct_init(self):
        self.assertEqual(self.driver.name, "TestName")
        self.assertEqual(self.driver.money_per_mile, 1)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_below_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), "TestName went bankrupt.")

    def test_add_cargo_offer_cargo_location_already_added_raise_Exception(self):

        self.driver.available_cargos = {"Sofia": 400, "Plovid": 600}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 400)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_location_not_added(self):

        self.driver.available_cargos = {"Sofia": 400, "Plovid": 600}
        result = self.driver.add_cargo_offer("Varna", 800)

        expected_result = f"Cargo for 800 to Varna was added as an offer."
        expected_dict = {"Sofia": 400, "Plovid": 600, "Varna": 800}

        self.assertEqual(result, expected_result)
        self.assertEqual(self.driver.available_cargos, expected_dict)

    def test_drive_best_cargo_offer_no_cargos(self):
        self.driver.available_cargos = {}
        result = self.driver.drive_best_cargo_offer()
        expected_result = "There are no offers available."

        self.assertEqual(result, expected_result)
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_drive_best_cargo_offer_10000(self):

        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Sofia": 10000, "Plovid": 600, "Varna": 800}
        result = self.driver.drive_best_cargo_offer()
        expected_result = f"{self.driver.name} is driving 10000 to Sofia."

        self.assertEqual(self.driver.earned_money, 38250)
        self.assertEqual(self.driver.miles, 10000)
        self.assertEqual(result, expected_result)

    def test_drive_best_cargo_offer_less_than_10000(self):

        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Sofia": 3000, "Plovid": 600, "Varna": 800}
        result = self.driver.drive_best_cargo_offer()
        expected_result = f"{self.driver.name} is driving 3000 to Sofia."

        self.assertEqual(self.driver.earned_money, 13625)
        self.assertEqual(self.driver.miles, 3000)
        self.assertEqual(result, expected_result)

    def test_drive_best_cargo_offer_less_than_1500(self):

        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Sofia": 1000, "Plovid": 600, "Varna": 800}
        result = self.driver.drive_best_cargo_offer()
        expected_result = f"{self.driver.name} is driving 1000 to Sofia."

        self.assertEqual(self.driver.earned_money, 4875)
        self.assertEqual(self.driver.miles, 1000)
        self.assertEqual(result, expected_result)

    def test_drive_best_cargo_offer_less_than_100(self):

        self.driver.money_per_mile = 5
        self.driver.available_cargos = {"Sofia": 750, "Plovid": 600, "Varna": 400}
        result = self.driver.drive_best_cargo_offer()
        expected_result = f"{self.driver.name} is driving 750 to Sofia."

        self.assertEqual(self.driver.earned_money, 3690)
        self.assertEqual(self.driver.miles, 750)
        self.assertEqual(result, expected_result)

    def test_repr(self):
        self.driver.miles = 7500

        result = repr(self.driver)
        expected_result = "TestName has 7500 miles behind his back."

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
