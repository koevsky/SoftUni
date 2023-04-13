from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):

        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = None
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)

        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        try:

            computer = next(filter(lambda c:
                                   c.price <= client_budget and
                                   c.processor == wanted_processor and
                                   c.ram >= wanted_ram,
                                   self.warehouse))

        except StopIteration:
            raise Exception("Sorry, we don't have a computer for you.")

        profit = client_budget - computer.price
        self.profits += profit
        message = str(computer)
        self.warehouse.remove(computer)
        return f"{message} sold for {client_budget}$."


