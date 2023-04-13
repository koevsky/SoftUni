from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    DEFAULT_OXYGEN = 50
    DEFAULT_BREATH_UNITS = 10

    def __init__(self, name):
        super().__init__(name, Geodesist.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= Geodesist.DEFAULT_BREATH_UNITS
