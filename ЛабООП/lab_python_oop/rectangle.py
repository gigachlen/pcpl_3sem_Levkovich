"""
Модуль содержит класс Rectangle (Прямоугольник)
"""

from .geometric_figure import GeometricFigure
from .color import Color


class Rectangle(GeometricFigure):
    """
    Класс Прямоугольник, наследуется от GeometricFigure
    """

    FIGURE_NAME = "Прямоугольник"

    def __init__(self, width, height, color):
        """
        Конструктор прямоугольника

        :param width: ширина
        :param height: высота
        :param color: цвет (строка)
        """
        self.width = width
        self.height = height
        self.figure_color = Color()
        self.figure_color.color = color

    def area(self):
        """
        Вычисление площади прямоугольника
        """
        return self.width * self.height

    @classmethod
    def get_figure_name(cls):
        """
        Возвращает название фигуры
        """
        return cls.FIGURE_NAME

    def __repr__(self):
        """
        Строковое представление прямоугольника
        """
        return "{} {} цвета со сторонами {} и {}, площадь: {:.2f}".format(
            self.get_figure_name(),
            self.figure_color.color,
            self.width,
            self.height,
            self.area()
        )