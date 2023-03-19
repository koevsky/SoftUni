from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, height, side):
        self.height = height
        self.side = side

    def calc_area(self):
        return 0.5 * self.height * self.side


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not type(value) == list:
            raise ValueError("Shapes mus be in a list !")

        self.__shapes = value

    @property
    def total_area(self):
        return sum([fig.calc_area() for fig in shapes])


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)


