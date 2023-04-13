from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):

    DEFAULT_MEMBERS = 1
    ROOM_COST = 10

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, AloneYoung.DEFAULT_MEMBERS)

        self.room_cost = AloneYoung.ROOM_COST
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)



