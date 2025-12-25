"""
Модуль содержит класс Circle (Круг)
"""

import math
from .geometric_figure import GeometricFigure
from .color import Color


class Circle(GeometricFigure):
    """
    Класс Круг, наследуется от GeometricFigure
    """

    FIGURE_NAME = "Круг"

    def __init__(self, radius, color):
        """
        Конструктор круга

        :param radius: радиус
        :param color: цвет (строка)
        """
        self.radius = radius
        self.figure_color = Color()
        self.figure_color.color = color

    def area(self):
        """
        Вычисление площади круга
        """
        return math.pi * self.radius ** 2

    @classmethod
    def get_figure_name(cls):
        """
        Возвращает название фигуры
        """
        return cls.FIGURE_NAME

    def __repr__(self):
        """
        Строковое представление круга
        """
        return "{} {} цвета с радиусом {}, площадь: {:.2f}".format(
            self.get_figure_name(),
            self.figure_color.color,
            self.radius,
            self.area()
        )