from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.biologist import Biologist
from project.astronaut.astronaut_repository import AstronautRepository

from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):

        if astronaut_type in ["Biologist", "Geodesist", "Meteorologist"]:

            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."

            astronaut = None
            if astronaut_type == "Biologist":
                astronaut = Biologist(name)

            elif astronaut_type == "Geodesist":
                astronaut = Geodesist(name)

            elif astronaut_type == "Meteorologist":
                astronaut = Meteorologist(name)

            self.astronaut_repository.add(astronaut)
            return f"Successfully added {astronaut_type}: {name}."

        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")

        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):

        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        [astronaut.increase_oxygen(10) for astronaut in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)

        if planet is None:
            raise Exception("Invalid planet name!")

        suitable_astronauts = list(filter(lambda ast: ast.oxygen > 30, self.astronaut_repository.astronauts))
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astronauts = list(sorted(suitable_astronauts, key=lambda ast: ast.oxygen, reverse=True))[:5]

        for num, astronaut in enumerate(suitable_astronauts):

            while planet.items:

                item = planet.items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()

                if not planet.items:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored. {num+1} astronauts participated in collecting items."

                if astronaut.oxygen <= 0:
                    break

        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):

        result = []

        result.append(f'{self.successful_missions} successful missions!')
        result.append(f'{self.not_completed_missions} missions were not completed!')
        result.append("Astronauts' info:")

        for astronaut in self.astronaut_repository.astronauts:

            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")

            backpack_string = f"Backpack items: "
            if astronaut.backpack:
                backpack_string += ", ".join(astronaut.backpack)
            else:
                backpack_string += 'none'
            result.append(backpack_string)

        return '\n'.join(result)














