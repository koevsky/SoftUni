from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):

    DEFAULT_MEMBERS = 2
    ROOM_COST = 15

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, OldCouple.DEFAULT_MEMBERS)

        self.room_cost = OldCouple.ROOM_COST
        self.appliances = [TV(), Fridge(), Stove()]
        self.calculate_expenses(self.appliances)


