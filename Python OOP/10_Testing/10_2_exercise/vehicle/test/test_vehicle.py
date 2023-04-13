from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTest(TestCase):

    def setUp(self) -> None:

        self.vehicle = Vehicle(10, 42)

    def test_correct_init(self):
        self.assertEqual(self.vehicle.fuel, 10)
        self.assertEqual(self.vehicle.horse_power, 42)
        self.assertEqual(self.vehicle.capacity, 10)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_insufficient_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.fuel_consumption = 1
        self.vehicle.drive(2)
        self.assertEqual(self.vehicle.fuel, 8)

    def test_too_mush_fuel_raise_exception(self):
        self.vehicle.fuel = 5

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_enough_quantity_fuel_added(self):
        self.vehicle.fuel = 5
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 10)

    def test_instance_string_return(self):
        expected = "The vehicle has 42 " \
                    "horse power with 10 fuel left" \
                    " and 1.25 fuel consumption"

        self.assertEqual(str(self.vehicle), expected)


if __name__ == '__main__':
    main()