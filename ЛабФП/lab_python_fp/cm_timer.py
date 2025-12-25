"""
Задача 6: Контекстные менеджеры для замера времени
"""

import time
from contextlib import contextmanager


# Способ 1: На основе класса
class cm_timer_1:
    """
    Контекстный менеджер для замера времени (реализация через класс).
    """

    def __enter__(self):
        """Вход в контекст - запоминаем время начала."""
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Выход из контекста - вычисляем и выводим время."""
        elapsed_time = time.time() - self._start_time
        print(f"time: {elapsed_time:.6f}")
        return False  # Не подавляем исключения


# Способ 2: С использованием contextlib
@contextmanager
def cm_timer_2():
    """
    Контекстный менеджер для замера времени (реализация через contextlib).
    """
    start_time = time.time()
    try:
        yield
    finally:
        elapsed_time = time.time() - start_time
        print(f"time: {elapsed_time:.6f}")


if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование контекстных менеджеров")
    print("=" * 50)

    print("\nТест cm_timer_1 (на основе класса):")
    print("Выполняем sleep(0.5)...")
    with cm_timer_1():
        time.sleep(0.5)

    print("\nТест cm_timer_2 (с использованием contextlib):")
    print("Выполняем sleep(0.3)...")
    with cm_timer_2():
        time.sleep(0.3)

    print("\nТест с вычислениями:")
    print("Вычисляем сумму чисел от 1 до 1000000...")
    with cm_timer_1():
        result = sum(range(1, 1000001))
    print(f"Результат: {result}")

    print("\nТест с генератором:")
    from .gen_random import gen_random

    print("Генерируем 100000 случайных чисел...")
    with cm_timer_2():
        numbers = list(gen_random(100000, 1, 1000))
    print(f"Сгенерировано {len(numbers)} чисел")