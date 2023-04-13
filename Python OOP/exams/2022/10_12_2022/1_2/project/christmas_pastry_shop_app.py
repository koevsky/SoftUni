from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth

from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if type_delicacy in ["Gingerbread", "Stolen"]:

            is_delicacy_name = list(filter(lambda d: d.name == name, self.delicacies))
            if is_delicacy_name:
                raise Exception(f"{name} already exists!")

            delicacies_dict = {

                "Gingerbread": Gingerbread(name, price),
                "Stolen": Stolen(name, price)

                               }

            delicacy = delicacies_dict[type_delicacy]

            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

        raise Exception(f"{type_delicacy} is not on our delicacy menu!")

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if type_booth in ["Open Booth", "Private Booth"]:

            is_boot_number = list(filter(lambda b: b.booth_number == booth_number, self.booths))
            if is_boot_number:
                raise Exception(f"Booth number {booth_number} already exists!")

            booths_dict = {

                "Open Booth": OpenBooth(booth_number, capacity),
                "Private Booth": PrivateBooth(booth_number, capacity)

                        }

            booth = booths_dict[type_booth]

            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."

        raise Exception(f"{type_booth} is not a valid booth!")

    def reserve_booth(self, number_of_people: int):
        try:
            booth = next(filter(lambda b: not b.is_reserved and number_of_people <= b.capacity, self.booths))

        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))

        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):

        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        orders_cost = sum([delicacy.price for delicacy in booth.delicacy_orders])
        bill = orders_cost + booth.price_for_reservation
        self.income += bill

        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False

        result = [f"Booth {booth_number}:", f"Bill: {bill:.2f}lv."]

        return '\n'.join(result)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."