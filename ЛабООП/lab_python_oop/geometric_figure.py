"""
Модуль содержит абстрактный класс GeometricFigure
"""

from abc import ABC, abstractmethod


class GeometricFigure(ABC):
    """
    Абстрактный класс для геометрических фигур
    """

    @abstractmethod
    def area(self):
        """
        Абстрактный метод для вычисления площади фигуры
        """
        pass