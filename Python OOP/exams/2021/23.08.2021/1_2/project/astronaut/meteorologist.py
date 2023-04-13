from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):

    DEFAULT_OXYGEN = 90
    DEFAULT_BREATH_UNITS = 15

    def __init__(self, name):
        super().__init__(name, Meteorologist.DEFAULT_OXYGEN)

    def breathe(self):
        self.oxygen -= Meteorologist.DEFAULT_BREATH_UNITS
