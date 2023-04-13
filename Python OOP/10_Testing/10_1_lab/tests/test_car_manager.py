from unittest import TestCase, main
from files.car_manager import Car


class CarTests(TestCase):

    def setUp(self) -> None:
        self.car = Car("Opel", "Astra-J", 7, 56)

    def test_correct_init(self):
        self.assertEqual("Opel", self.car.make)
        self.assertEqual("Astra-J", self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(56, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_less_or_equal_to_tank_capacity(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_more_than_fuel_capacity(self):
        self.car.refuel(70)
        self.assertEqual(56, self.car.fuel_amount)

    def test_drive_car_with_insufficient_amount_of_fuel_raise_exception(self):
        self.car.fuel_amount = 7

        with self.assertRaises(Exception) as ex:
            self.car.drive(200)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_enough_fuel(self):
        self.car.fuel_amount = 14
        self.car.drive(200)

        self.assertEqual(0, self.car.fuel_amount)


if __name__ == '__main__':
    main()