from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):

    DEFAULT_PORTION = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, Cake.DEFAULT_PORTION, price)


