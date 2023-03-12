from project.animals.animal import Bird


class Owl(Bird):

    WEIGHT_GROWTH = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity


class Hen(Bird):

    WEIGHT_GROWTH = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += self.WEIGHT_GROWTH * food.quantity

