from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False

    def find_by_type(self, decoration_type: str):

        for dec in self.decorations:
            if dec.__class__.__name__ == decoration_type:
                return dec

        return "None"
