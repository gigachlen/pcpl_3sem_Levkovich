"""
Главный модуль для тестирования классов геометрических фигур
"""

from lab_python_oop import Rectangle, Circle, Square
from colorama import init, Fore, Style

# Инициализация colorama для цветного вывода
init(autoreset=True)


def main():
    """
    Основная функция программы
    """
    # Номер варианта (замените на свой номер по списку)
    N = 5

    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "Лабораторная работа №2: ООП в Python")
    print(Fore.CYAN + "=" * 60 + "\n")

    # Создание прямоугольника
    rectangle = Rectangle(N, N, "синий")
    print(Fore.BLUE + str(rectangle))

    # Создание круга
    circle = Circle(N, "зеленый")
    print(Fore.GREEN + str(circle))

    # Создание квадрата
    square = Square(N, "красный")
    print(Fore.RED + str(square))

    print("\n" + Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "Демонстрация работы внешнего пакета colorama:")
    print(Fore.MAGENTA + "Этот текст выведен разными цветами!" + Style.RESET_ALL)
    print(Fore.CYAN + "=" * 60)


if __name__ == "__main__":
    main()