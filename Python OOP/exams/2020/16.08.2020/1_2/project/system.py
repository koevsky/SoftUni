from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware

from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)

        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)

        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        try:
            hardware = next(filter(lambda hw: hw.name == hardware_name, System._hardware))

        except StopIteration:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        try:
            hardware = next(filter(lambda hw: hw.name == hardware_name, System._hardware))

        except StopIteration:
            return "Hardware does not exist"

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        is_hardware = list(filter(lambda hw: hw.name == hardware_name, System._hardware))
        is_software = list(filter(lambda sw: sw.name == software_name, System._software))

        if is_hardware and is_software:

            hardware = is_hardware[0]
            software = is_software[0]

            if software in hardware.software_components:
                hardware.uninstall(software)

            System._software.remove(software)

        return f"Some of the components do not exist"

    @staticmethod
    def analyze():

        result = ["System Analysis"]

        result.append(f"Hardware Components: {len(System._hardware)}")
        result.append(f"Software Components: {len(System._software)}")
        result.append(f"Total Operational Memory: {sum([software.memory_consumption for software in System._software])} "
                      f"/ {sum([hardware.memory for hardware in System._hardware])}")

        result.append(f"Total Capacity Taken: {sum([software.capacity_consumption for software in System._software])} /"
                      f" {sum([hardware.capacity for hardware in System._hardware])}")

        return '\n'.join(result)

    @staticmethod
    def system_split():

        result = []

        for hardware in System._hardware:

            express_software_count = len(list(filter(lambda esw: esw.software_type == "Express", hardware.software_components)))
            light_software_count = len(list(filter(lambda esw: esw.software_type == "Light", hardware.software_components)))
            total_memory_used = sum([software.memory_consumption for software in hardware.software_components])
            total_capacity_used = sum([software.capacity_consumption for software in hardware.software_components])

            text = ', '.join([software.name for software in hardware.software_components])

            result.append(f"Hardware Component - {hardware.name}")
            result.append(f"Express Software Components: {express_software_count}")
            result.append(f"Light Software Components: {light_software_count}")
            result.append(f"Memory Usage: {total_memory_used} / {hardware.memory}")
            result.append(f"Capacity Usage: {total_capacity_used} / {hardware.capacity}")
            result.append(f"Type: {hardware.hardware_type}")
            if text:
                result.append(f"Software Components: {text}")
            else:
                result.append(f"Software Components: None")

        return "\n".join(result)












