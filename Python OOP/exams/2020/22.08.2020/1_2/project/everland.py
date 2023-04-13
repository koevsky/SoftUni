from project.rooms.room import Room
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren

from project.people.child import Child

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.appliances.stove import Stove
from project.appliances.laptop import Laptop
from project.appliances.fridge import Fridge


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):

        total_consumption = sum([room.expenses + room.room_cost for room in self.rooms])

        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):

        result = []

        index = 0

        while index < len(self.rooms):

            room = self.rooms[index]

            if room.expenses + room.room_cost > room.budget:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.pop(index)

            else:
                money_paid = room.expenses + room.room_cost
                room.budget -= money_paid
                result.append(f"{room.family_name} paid {money_paid:.2f}$ and have {room.budget:.2f}$ left.")
                index += 1

        return '\n'.join(result)

    def status(self):

        total_population = sum([room.members_count for room in self.rooms])

        result = [f"Total population: {total_population}"]

        for room in self.rooms:

            name = room.family_name
            members = room.members_count
            budget = room.budget
            expenses = room.expenses

            result.append(f"{name} with {members} members. Budget: {budget:.2f}$, Expenses: {expenses:.2f}$")

            if room.children:

                for number, child in enumerate(room.children):

                    child_cost = child.cost * 30

                    result.append(f"--- Child {number+1} monthly cost: {child_cost:.2f}$")

            if hasattr(room, "appliances"):

                total_app = sum([app.get_monthly_expense() * room.members_count for app in room.appliances])

                result.append(f"--- Appliances monthly cost: {total_app:.2f}$")

        return '\n'.join(result)











