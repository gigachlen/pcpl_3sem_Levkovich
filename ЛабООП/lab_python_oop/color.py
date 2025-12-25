"""
Модуль содержит класс Color для работы с цветом фигуры
"""


class Color:
    """
    Класс для описания цвета геометрической фигуры
    """

    def __init__(self):
        self._color = None

    @property
    def color(self):
        """
        Свойство для получения цвета
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Свойство для установки цвета
        """
        self._color = value