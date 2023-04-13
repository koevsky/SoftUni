from project.software.software import Software
import math


class LightSoftware(Software):

    DEFAULT_TYPE = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, LightSoftware.DEFAULT_TYPE, capacity_consumption, memory_consumption)
        self.capacity_consumption = math.floor(capacity_consumption + (capacity_consumption * 50/100))
        self.memory_consumption = math.floor(memory_consumption - (memory_consumption * 50/100))


