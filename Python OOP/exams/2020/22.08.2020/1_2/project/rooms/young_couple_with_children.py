from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):

    DEFAULT_MEMBERS = 2
    ROOM_COST = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one+salary_two, (len(children) + YoungCoupleWithChildren.DEFAULT_MEMBERS))

        self.room_cost = YoungCoupleWithChildren.ROOM_COST
        self.appliances = [TV(), Fridge(), Laptop()]
        self.children = children
        self.calculate_expenses(self.appliances, self.children)



