from abc import ABC, abstractmethod
import math


class Computer(ABC):

    AVAILABLE_PROCESSORS = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value or value.isspace():
            raise ValueError("Manufacturer name cannot be empty.")
        
        self.__manufacturer = value
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value: str):
        if not value or value.isspace():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @staticmethod
    def is_power_of_two(n):
        return str(math.log(n, 2)).endswith(".0")

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
