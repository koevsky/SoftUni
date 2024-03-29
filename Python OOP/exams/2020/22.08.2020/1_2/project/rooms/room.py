from project.people.child import Child
from project.appliances.appliance import Appliance


class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count

        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value: float):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):

        total_cost = 0

        for lst in args:

            for el in lst:

                if isinstance(el, Child):
                    total_cost += el.cost * 30

                elif isinstance(el, Appliance):
                    total_cost += el.get_monthly_expense() * self.members_count

        self.expenses = total_cost






