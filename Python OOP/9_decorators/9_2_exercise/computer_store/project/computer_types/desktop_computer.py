from project.computer_types.computer import Computer
import math


class DesktopComputer(Computer):

    AVAILABLE_PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.AVAILABLE_PROCESSORS.keys():
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if not (self.is_power_of_two(ram) and ram in range(2, 129)):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        total_price = int(math.log(ram, 2)) * 100 + self.AVAILABLE_PROCESSORS[processor]

        self.processor = processor
        self.ram = ram
        self.price = total_price

        return f"Created {self.manufacturer} {self.model} with {self.processor} and {ram}GB RAM for {total_price}$."

