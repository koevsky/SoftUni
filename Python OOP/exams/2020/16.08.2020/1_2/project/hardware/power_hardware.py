from project.hardware.hardware import Hardware
import math


class PowerHardware(Hardware):

    DEFAULT_TYPE = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, PowerHardware.DEFAULT_TYPE, capacity, memory)
        self.capacity = math.floor(capacity * 25/100)
        self.memory = math.floor(memory + (memory * 75/100))

