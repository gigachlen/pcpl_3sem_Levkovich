"""
Задача 2: Генератор случайных чисел gen_random
"""

import random


# Пример:
# gen_random(5, 1, 3) должен выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
# Hint: типовая реализация занимает 2 строки


def gen_random(num_count, begin, end):
    """
    Генератор случайных чисел.

    Args:
        num_count: количество чисел
        begin: минимальное значение (включительно)
        end: максимальное значение (включительно)

    Yields:
        Случайные числа в заданном диапазоне
    """
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование генератора gen_random")
    print("=" * 50)

    print("\ngen_random(5, 1, 3):")
    result = list(gen_random(5, 1, 3))
    print(f"  {result}")

    print("\ngen_random(10, 1, 100):")
    result = list(gen_random(10, 1, 100))
    print(f"  {result}")

    print("\ngen_random(3, -5, 5):")
    result = list(gen_random(3, -5, 5))
    print(f"  {result}")

    # Демонстрация работы с генератором напрямую
    print("\nПоследовательная итерация gen_random(5, 10, 20):")
    for i, num in enumerate(gen_random(5, 10, 20), 1):
        print(f"  Число {i}: {num}")