from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):

    DEFAULT_MEMBERS = 2
    ROOM_COST = 20

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one+salary_two, YoungCouple.DEFAULT_MEMBERS)

        self.room_cost = YoungCouple.ROOM_COST
        self.appliances = [TV(), Fridge(), Laptop()]
        self.calculate_expenses(self.appliances)