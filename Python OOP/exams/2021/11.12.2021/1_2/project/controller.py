from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race
from project.driver import Driver


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if car_type in ['MuscleCar', 'SportsCar']:

            is_model = list(filter(lambda c: c.model == model, self.cars))
            if is_model:
                raise Exception(f"Car {model} is already created!")

            car = None
            if car_type == 'MuscleCar':
                car = MuscleCar(model, speed_limit)

            elif car_type == 'SportsCar':
                car = SportsCar(model, speed_limit)

            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        is_driver = list(filter(lambda d: d.name == driver_name, self.drivers))
        if is_driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):

        is_race = list(filter(lambda r: r.name == race_name, self.races))
        if is_race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))

        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = next(filter(lambda c: c.__class__.__name__ == car_type and not c.is_taken, list(reversed(self.cars))))

        except StopIteration:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:

            old_model = driver.car.model
            new_model = car.model

            driver.car.is_taken = False

            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):

        try:
            race = next(filter(lambda r: r.name == race_name, self.races))

        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))

        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):

        try:
            race = next(filter(lambda r: r.name == race_name, self.races))

        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        top_3 = list(sorted(race.drivers, key=lambda dr: dr.car.speed_limit, reverse=True))

        result = []

        for driver in top_3[:3]:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(result)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]











