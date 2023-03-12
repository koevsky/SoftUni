from project.animals.animal import Mammal


class Mouse(Mammal):

    WEIGHT_GROWTH = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):

        if food.__class__.__name__ not in ['Vegetable', 'Fruit']:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity


class Dog(Mammal):

    WEIGHT_GROWTH = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ != 'Meat':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity


class Cat(Mammal):

    WEIGHT_GROWTH = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in ['Meat', 'Vegetable']:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity


class Tiger(Mammal):

    WEIGHT_GROWTH = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ != 'Meat':
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity

