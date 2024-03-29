from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink

from abc import ABC


class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError(f"Capacity has to be greater than 0!")

        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):

        food_bill = sum([f.price for f in self.food_orders])
        drink_bill = sum(d.price for d in self.drink_orders)

        total_bill = food_bill + drink_bill
        return total_bill

    def clear(self):

        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):

        if not self.is_reserved:

            result = [f"Table: {self.table_number}", f"Type: {self.__class__.__name__}", f"Capacity: {self.capacity}"]
            return '\n'.join(result)




