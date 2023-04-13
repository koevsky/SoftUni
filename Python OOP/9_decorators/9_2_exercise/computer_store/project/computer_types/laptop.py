from project.computer_types.computer import Computer
import math


class Laptop(Computer):

    AVAILABLE_PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}


    def configure_computer(self, processor: str, ram: int):

        if processor not in self.AVAILABLE_PROCESSORS.keys():
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if not (self.is_power_of_two(ram) and ram in range(2, 65)):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        total_price = int(math.log(ram, 2)) * 100 + self.AVAILABLE_PROCESSORS[processor]

        self.processor = processor
        self.ram = ram
        self.price = total_price

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {ram}GB RAM for {total_price}$."
