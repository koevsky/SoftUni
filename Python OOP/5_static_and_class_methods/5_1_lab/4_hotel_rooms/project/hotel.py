class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number, people) -> str or None:
        room = next(filter(lambda r: r.number == room_number, self.rooms))

        if not room.take_room(people):
            self.guests += people

    def free_room(self, room_number) -> str or None:
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        guests = room.guests
        if not room.free_room():
            self.guests -= guests

    def status(self):

        result = [f"Hotel {self.name} has {self.guests} total guests"]
        result.append(f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}")
        result.append(f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}")

        return '\n'.join(result)
