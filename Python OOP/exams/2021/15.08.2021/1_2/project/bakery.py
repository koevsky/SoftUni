from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

from project.baked_food.cake import Cake
from project.baked_food.bread import Bread

from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:

    def __init__(self, name: str):
        self.name = name

        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ["Bread", "Cake"]:

            is_food = list(filter(lambda f: f.name == name, self.food_menu))
            if is_food:
                raise Exception(f"{food_type} {name} is already in the menu!")

            food = None
            if food_type == "Bread":
                food = Bread(name, price)

            elif food_type == "Cake":
                food = Cake(name, price)

            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ["Tea", "Water"]:

            is_drink = list(filter(lambda d: d.name == name, self.drinks_menu))
            if is_drink:
                raise Exception(f"{drink_type} {name} is already in the menu!")

            drink = None
            if drink_type == "Tea":
                drink = Tea(name, portion, brand)

            elif drink_type == "Water":
                drink = Water(name, portion, brand)

            self.drinks_menu.extend([drink])
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ["InsideTable", "OutsideTable"]:

            is_table = list(filter(lambda t: t.table_number == table_number, self.tables_repository))
            if is_table:
                raise Exception(f"Table {table_number} is already in the bakery!")

            table = None
            if table_type == "InsideTable":
                table = InsideTable(table_number, capacity)

            elif table_type == "OutsideTable":
                table = OutsideTable(table_number, capacity)

            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):

        try:
            table = next(filter(lambda t: not t.is_reserved and t.capacity >= number_of_people, self.tables_repository))

        except StopIteration:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *food):
        try:
            table = next(filter(lambda t: t.table_number == table_number, self.tables_repository))

        except StopIteration:
            return f"Could not find table {table_number}"

        valid_food = []
        invalid_food = []

        for food_name in food:

            is_food = list(filter(lambda f: f.name == food_name, self.food_menu))

            if is_food:

                food = is_food[0]
                table.order_food(food)
                valid_food.append(food)

            else:
                invalid_food.append(food_name)

        result = [f"Table {table_number} ordered:"]
        [result.append(repr(f)) for f in valid_food]

        result.append(f"{self.name} does not have in the menu:")
        [result.append(n) for n in invalid_food]

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks):
        try:
            table = next(filter(lambda t: t.table_number == table_number, self.tables_repository))

        except StopIteration:
            return f"Could not find table {table_number}"

        valid_drinks = []
        invalid_drinks = []

        for drink_name in drinks:

            is_drink = list(filter(lambda d: d.name == drink_name, self.drinks_menu))

            if is_drink:

                drink = is_drink[0]
                table.order_drink(drink)
                valid_drinks.append(drink)

            else:
                invalid_drinks.append(drink_name)

        result = [f"Table {table_number} ordered:"]
        [result.append(str(d)) for d in valid_drinks]

        result.append(f"{self.name} does not have in the menu:")
        [result.append(n) for n in invalid_drinks]

        return '\n'.join(result)

    def leave_table(self, table_number: int):

        is_table = list(filter(lambda t: t.table_number == table_number, self.tables_repository))

        if is_table:

            table = is_table[0]
            bill = table.get_bill()
            self.total_income += bill

            table.clear()

            return f"Table: {table.table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = [table.free_table_info() for table in self.tables_repository]

        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"










