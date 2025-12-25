"""
Задача 5: Декоратор print_result
"""

from functools import wraps


def print_result(func):
    """
    Декоратор, который выводит на экран результат выполнения функции.

    - Печатает имя функции и результат выполнения
    - Если результат - список (list), значения выводятся в столбик
    - Если результат - словарь (dict), ключи и значения выводятся через '='

    Args:
        func: декорируемая функция

    Returns:
        Обёрнутая функция
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Вызываем функцию
        result = func(*args, **kwargs)

        # Печатаем имя функции
        print(func.__name__)

        # Печатаем результат в зависимости от типа
        if isinstance(result, list):
            # Список - выводим в столбик
            for item in result:
                print(item)
        elif isinstance(result, dict):
            # Словарь - выводим ключи и значения через '='
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            # Остальные типы - просто выводим
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование декоратора print_result")
    print("=" * 50)
    print()
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()