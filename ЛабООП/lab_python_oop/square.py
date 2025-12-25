"""
Модуль содержит класс Square (Квадрат)
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Класс Квадрат, наследуется от Rectangle
    """

    FIGURE_NAME = "Квадрат"

    def __init__(self, side, color):
        """
        Конструктор квадрата

        :param side: длина стороны
        :param color: цвет (строка)
        """
        super().__init__(side, side, color)
        self.side = side

    def __repr__(self):
        """
        Строковое представление квадрата
        """
        return "{} {} цвета со стороной {}, площадь: {:.2f}".format(
            self.get_figure_name(),
            self.figure_color.color,
            self.side,
            self.area()
        )