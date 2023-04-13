from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot

from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):

        if service_type in ["MainService", "SecondaryService"]:

            service_dict = {"MainService": MainService(name), "SecondaryService": SecondaryService(name)}
            service = service_dict[service_type]

            self.services.append(service)
            return f"{service_type} is successfully added."

        raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type in ["MaleRobot", "FemaleRobot"]:

            robots_dict = {"MaleRobot": MaleRobot(name, kind, price), "FemaleRobot": FemaleRobot(name, kind, price)}
            robot = robots_dict[robot_type]

            self.robots.append(robot)
            return f"{robot_type} is successfully added."

        raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str):

        robot = next(filter(lambda rob: rob.name == robot_name, self.robots))
        service = next(filter(lambda svc: svc.name == service_name, self.services))

        robot_type = robot.__class__.__name__
        service_type = service.__class__.__name__

        if robot_type == "MaleRobot" and service_type != "MainService":
            return "Unsuitable service."

        elif robot_type == "FemaleRobot" and service_type != "SecondaryService":
            return "Unsuitable service."

        if service.capacity == len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = next(filter(lambda svc: svc.name == service_name, self.services))

        try:
            robot = next(filter(lambda rob: rob.name == robot_name, service.robots))

        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):

        service = next(filter(lambda svc: svc.name == service_name, self.services))

        [rob.eating() for rob in service.robots]
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):

        service = next(filter(lambda svc: svc.name == service_name, self.services))

        total_price = sum([rob.price for rob in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):

        result = [svc.details() for svc in self.services]

        return '\n'.join(result)







