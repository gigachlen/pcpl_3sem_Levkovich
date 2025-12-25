"""
Задача 3: Итератор Unique для удаления дубликатов
"""

from .gen_random import gen_random


class Unique:
    """
    Итератор для удаления дубликатов.

    Поддерживает работу как со списками, так и с генераторами.
    """

    def __init__(self, items, **kwargs):
        """
        Конструктор итератора.

        Args:
            items: список или генератор
            **kwargs:
                ignore_case (bool): если True, строки в разном регистре
                                   считаются одинаковыми. По умолчанию False.
        """
        self._items = iter(items)
        self._ignore_case = kwargs.get('ignore_case', False)
        self._seen = set()

    def __next__(self):
        """
        Возвращает следующий уникальный элемент.

        Returns:
            Следующий уникальный элемент

        Raises:
            StopIteration: когда элементы закончились
        """
        while True:
            item = next(self._items)  # Может выбросить StopIteration

            # Определяем ключ для сравнения
            if self._ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            # Проверяем, видели ли мы этот элемент
            if key not in self._seen:
                self._seen.add(key)
                return item  # Возвращаем оригинальное значение

    def __iter__(self):
        return self


if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование итератора Unique")
    print("=" * 50)

    # Тест 1: числа
    print("\nТест 1: Числа с дубликатами")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(f"  Исходные данные: {data}")
    print(f"  Unique(data): {list(Unique(data))}")

    # Тест 2: работа с генератором
    print("\nТест 2: Работа с генератором gen_random(10, 1, 3)")
    result = list(Unique(gen_random(10, 1, 3)))
    print(f"  Unique(gen_random(10, 1, 3)): {result}")

    # Тест 3: строки без ignore_case
    print("\nТест 3: Строки без ignore_case")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"  Исходные данные: {data}")
    print(f"  Unique(data): {list(Unique(data))}")

    # Тест 4: строки с ignore_case=True
    print("\nТест 4: Строки с ignore_case=True")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(f"  Исходные данные: {data}")
    print(f"  Unique(data, ignore_case=True): {list(Unique(data, ignore_case=True))}")

    # Тест 5: смешанные данные
    print("\nТест 5: Смешанные данные")
    data = ['Привет', 'привет', 'ПРИВЕТ', 'Мир', 'МИР']
    print(f"  Исходные данные: {data}")
    print(f"  Unique(data): {list(Unique(data))}")
    print(f"  Unique(data, ignore_case=True): {list(Unique(data, ignore_case=True))}")

    # Тест 6: проверка, что значения не модифицируются
    print("\nТест 6: Проверка сохранения регистра при ignore_case=True")
    data = ['ABC', 'abc', 'Abc', 'DEF', 'def']
    print(f"  Исходные данные: {data}")
    result = list(Unique(data, ignore_case=True))
    print(f"  Unique(data, ignore_case=True): {result}")
    print(f"  (Сохранен оригинальный регистр первого вхождения)")