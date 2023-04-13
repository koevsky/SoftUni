from project.software.software import Software
import math


class ExpressSoftware(Software):

    DEFAULT_TYPE = "Express"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, ExpressSoftware.DEFAULT_TYPE, capacity_consumption, memory_consumption)
        self.memory_consumption *= 2

