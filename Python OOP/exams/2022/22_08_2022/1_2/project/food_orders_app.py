from typing import List

from project.client import Client

from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.starter import Starter
from project.meals.main_dish import MainDish


class FoodOrdersApp:

    receipt_id = 1

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):

        is_number_registered = list(filter(lambda client: client.phone_number == client_phone_number, self.clients_list))
        if is_number_registered:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:

            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:

                self.menu.append(meal)

    def show_menu(self):

        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []
        [result.append(meal.details()) for meal in self.menu]
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if self.show_menu():

            current_bill = 0
            ordered = []
            desired_items_dict = {}

            is_client = list(filter(lambda clt: clt.phone_number == client_phone_number, self.clients_list))
            if not is_client:
                self.register_client(client_phone_number)

            client = next(filter(lambda clt: clt.phone_number == client_phone_number, self.clients_list))

            for meal_name, desired_quantity in meal_names_and_quantities.items():

                try:
                    meal = next(filter(lambda m: m.name == meal_name, self.menu))

                except StopIteration:
                    raise Exception(f"{meal_name} is not on the menu!")

                meal_type = meal.__class__.__name__

                if meal.quantity < desired_quantity:
                    raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")

                current_bill += meal.price * desired_quantity
                ordered.append(meal)

                if meal.name not in desired_items_dict:
                    desired_items_dict[meal.name] = 0

                desired_items_dict[meal.name] += desired_quantity

            for meal in ordered:
                if meal.name not in client.orders_dict:

                    client.orders_dict[meal.name] = 0
                    client.shopping_cart.append(meal)

                client.orders_dict[meal.name] += desired_items_dict[meal.name]

                meal.quantity -= desired_items_dict[meal.name]

            client.bill += current_bill

            meal_names = ", ".join([meal.name for meal in client.shopping_cart])
            return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client = next(filter(lambda clt: clt.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:

            meal.quantity += client.orders_dict[meal.name]

        client.bill = 0
        client.orders_dict = {}
        client.shopping_cart.clear()
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):

        client = next(filter(lambda clt: clt.phone_number == client_phone_number, self.clients_list))

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        paid_money = client.bill
        current_id = FoodOrdersApp.receipt_id

        FoodOrdersApp.receipt_id += 1
        client.bill = 0
        client.shopping_cart.clear()
        client.orders_dict = {}

        return f"Receipt #{current_id} with total amount of {paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."





















