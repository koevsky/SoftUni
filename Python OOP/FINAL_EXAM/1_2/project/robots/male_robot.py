from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    DEFAULT_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.DEFAULT_WEIGHT)

    def eating(self):
        self.weight += 3