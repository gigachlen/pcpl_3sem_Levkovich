"""
Задача 7: Обработка данных с использованием всех инструментов
"""

import json
import sys
import os

# Импортируем наши инструменты
from .field import field
from .gen_random import gen_random
from .unique import Unique
from .print_result import print_result
from .cm_timer import cm_timer_1

# Получаем путь к файлу данных
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    # Путь по умолчанию - в той же директории, что и скрипт
    path = os.path.join(os.path.dirname(__file__), '..', 'data_light.json')


@print_result
def f1(arg):
    """
    Выводит отсортированный список профессий без повторений.
    Строки в разном регистре считаются равными.
    Сортировка игнорирует регистр.
    """
    return sorted(Unique(field(arg, 'job-name'), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    """
    Фильтрует входной массив, возвращая только элементы,
    начинающиеся со слова "программист" (без учета регистра).
    """
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    """
    Модифицирует каждый элемент массива, добавив строку "с опытом Python".
    """
    return list(map(lambda x: f"{x} с опытом Python", arg))


@print_result
def f4(arg):
    """
    Генерирует для каждой специальности зарплату от 100000 до 200000 рублей
    и присоединяет её к названию специальности.
    """
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]


if __name__ == '__main__':
    print("=" * 60)
    print("Обработка данных из файла")
    print("=" * 60)

    # Проверяем наличие файла
    if not os.path.exists(path):
        print(f"\nОшибка: Файл '{path}' не найден!")
        print("\nСоздаём тестовый файл data_light.json...")

        # Создаём тестовые данные
        test_data = [
            {"job-name": "Программист Python"},
            {"job-name": "Программист Java"},
            {"job-name": "программист C#"},
            {"job-name": "ПРОГРАММИСТ JavaScript"},
            {"job-name": "Дизайнер"},
            {"job-name": "Менеджер проектов"},
            {"job-name": "Программист Python"},  # дубликат
            {"job-name": "Аналитик данных"},
            {"job-name": "Программист Go"},
            {"job-name": "DevOps инженер"}
        ]

        # Сохраняем тестовые данные
        test_path = os.path.join(os.path.dirname(__file__), '..', 'data_light.json')
        with open(test_path, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)

        path = test_path
        print(f"Тестовый файл создан: {path}\n")

    # Загружаем данные
    print(f"Загружаем данные из: {path}\n")
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    print(f"Загружено {len(data)} записей\n")
    print("-" * 60)

    # Выполняем цепочку функций с замером времени
    with cm_timer_1():
        f4(f3(f2(f1(data))))