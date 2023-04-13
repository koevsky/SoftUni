from abc import ABC
from project.fish.base_fish import BaseFish
from project.decoration.base_decoration import BaseDecoration


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        
        self.__name = value

    def calculate_comfort(self):
        result = sum([decoration.comfort for decoration in self.decorations])
        return result

    def add_fish(self, fish: BaseFish):

        fish_type = fish.__class__.__name__
        if fish_type in ["FreshwaterFish", "SaltwaterFish"]:

            if len(self.fish) < self.capacity:
                self.fish.append(fish)

                return f"Successfully added {fish_type} to {self.name}."

            else:
                return "Not enough capacity."

    def remove_fish(self, fish: BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):

        result = [f"{self.name}:"]

        if self.fish:
            result.append(f"Fish: {' '.join([fish.name for fish in self.fish])}")
        else:
            result.append(f"Fish: none")

        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return '\n'.join(result)








