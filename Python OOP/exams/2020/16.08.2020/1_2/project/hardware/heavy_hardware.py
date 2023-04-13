from project.hardware.hardware import Hardware
import math


class HeavyHardware(Hardware):

    DEFAULT_TYPE = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, HeavyHardware.DEFAULT_TYPE, capacity, memory)
        self.capacity *= 2
        self.memory = math.floor(memory * 75/100)  # may be wrong

