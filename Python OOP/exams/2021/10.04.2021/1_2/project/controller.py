from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.decoration.decoration_repository import DecorationRepository


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):

        if aquarium_type in ["FreshwaterAquarium", "SaltwaterAquarium"]:

            aquarium = None
            if aquarium_type == "FreshwaterAquarium":
                aquarium = FreshwaterAquarium(aquarium_name)

            elif aquarium_type == "SaltwaterAquarium":
                aquarium = SaltwaterAquarium(aquarium_name)

            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."

        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):

        if decoration_type in ["Ornament", "Plant"]:

            decoration = None
            if decoration_type == "Ornament":
                decoration = Ornament()

            elif decoration_type == "Plant":
                decoration = Plant()

            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."

        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        is_aquarium = list(filter(lambda a: a.name == aquarium_name, self.aquariums))
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration != "None" and is_aquarium:
            aquarium = is_aquarium[0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        is_aquarium = list(filter(lambda a: a.name == aquarium_name, self.aquariums))

        if fish_type in ["FreshwaterFish", "SaltwaterFish"] and is_aquarium:

            aquarium = is_aquarium[0]
            aquarium_type = aquarium.__class__.__name__

            if aquarium_type == "FreshwaterAquarium" and fish_type != "FreshwaterFish":
                return "Water not suitable."

            if aquarium_type == "SaltwaterAquarium" and fish_type != "SaltwaterFish":
                return "Water not suitable."

            fish = None
            if fish_type == "FreshwaterFish":
                fish = FreshwaterFish(fish_name, fish_species, price)

            elif fish_type == "SaltwaterFish":
                fish = SaltwaterFish(fish_name, fish_species, price)

            return aquarium.add_fish(fish)

        return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):

        is_aquarium = list(filter(lambda a: a.name == aquarium_name, self.aquariums))
        if is_aquarium:
            aquarium = is_aquarium[0]

            aquarium.feed()

            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):

        is_aquarium = list(filter(lambda a: a.name == aquarium_name, self.aquariums))
        if is_aquarium:
            aquarium = is_aquarium[0]

            decorations_price = sum([decoration.price for decoration in aquarium.decorations])
            fish_price = sum([fish.price for fish in aquarium.fish])

            total = decorations_price + fish_price

            return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):

        result = [str(aquarium) for aquarium in self.aquariums]

        return '\n'.join(result)


controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "FirstFreshAqua"))
print(controller.add_aquarium("SaltwaterAquarium", "FirstSaltyAqua"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Vase"))
print(controller.decorations_repository.decorations)

print(controller.insert_decoration("FirstFreshAqua", "Plant"))
print(controller.insert_decoration("FirstFreshAqua", "Ornament"))
print(controller.insert_decoration("FirstFreshAqua", "Ornament"))
print(controller.insert_decoration("FirstFreshAqua", "Ornament"))

print(controller.add_fish("FirstFreshAqua", "FreshwaterFish", "Bob", "RedFish", 20))
print(controller.add_fish("FirstFreshAqua", "FreshwaterFish", "John", "RedFish", 20))
print(controller.add_fish("FirstFreshAqua", "FreshwaterFish", "Mike", "RedFish", 20))

print(controller.feed_fish("FirstFreshAqua"))
print(controller.aquariums[0].decorations)
print(controller.calculate_value("FirstFreshAqua"))
print(controller.report())








