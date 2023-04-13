from project.rooms.room import Room


class AloneOld(Room):

    DEFAULT_MEMBERS = 1
    ROOM_COST = 10

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, AloneOld.DEFAULT_MEMBERS)

        self.room_cost = AloneOld.ROOM_COST
        self.calculate_expenses()

