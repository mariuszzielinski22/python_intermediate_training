import abc
from math import pi


class Figure(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass

    @staticmethod
    def count_area(figures: list) -> float:
        area = 0.0
        for figure in figures:
            area += figure.get_area()
        return area

    @staticmethod
    def comparing_area(area: float, figures: list) -> bool:
        figure_area = Figure.count_area(figures)
        return area > figure_area
        # if area >= figure_area:
        #     print("It is enough wall paint to cover all this figures")
        # else:
        #     print("Sorry, you have to buy more wall paint.")


# to jest pozaklasą
def count_area_func(*args):
    area = 0.0
    for arg in args:
        area += arg.get_area()
    return area


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(pi * self.r ** 2, 2)


class Triangle(Figure):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def get_area(self):
        return (self.a * self.h) / 2


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b