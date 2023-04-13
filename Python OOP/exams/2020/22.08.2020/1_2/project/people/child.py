class Child:

    def __init__(self, food_cost: int, *toys_cost):
        self.cost = sum([toy for toy in toys_cost]) + food_cost
