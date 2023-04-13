from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> [object, None]:

        is_astronaut = list(filter(lambda ast: ast.name == name, self.astronauts))
        if is_astronaut:
            return is_astronaut[0]


