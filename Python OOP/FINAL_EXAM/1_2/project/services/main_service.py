from project.services.base_service import BaseService


class MainService(BaseService):

    DEFAULT_CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.DEFAULT_CAPACITY)

    def details(self):

        result = [f"{self.name} Main Service:"]

        if self.robots:

            robots = " ".join([robot.name for robot in self.robots])
            result.append(f"Robots: {robots}")

        else:
            result.append(f"Robots: none")

        return '\n'.join(result)




