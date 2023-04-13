from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory

        self.software_components = []

    def install(self, software: Software):
        memory_taken = sum([software.memory_consumption for software in self.software_components])
        capacity_taken = sum([software.capacity_consumption for software in self.software_components])

        condition_one = memory_taken + software.memory_consumption <= self.memory
        condition_two = capacity_taken + software.capacity_consumption <= self.capacity

        if condition_one and condition_two:

            self.software_components.append(software)

        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)





