"""
Задача 1: Генератор field
"""


# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def field(items, *args):
    """
    Генератор, последовательно выдающий значения ключей словаря.

    Args:
        items: список словарей
        *args: ключи для извлечения

    Yields:
        Если один ключ - значение поля
        Если несколько ключей - словарь с указанными полями
    """
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            # Один аргумент - выдаем только значение
            key = args[0]
            value = item.get(key)
            if value is not None:
                yield value
        else:
            # Несколько аргументов - выдаем словарь
            result = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
            # Пропускаем элемент, если все поля None
            if result:
                yield result


if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование генератора field")
    print("=" * 50)

    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    print("\nИсходные данные:")
    for item in goods:
        print(f"  {item}")

    print("\nfield(goods, 'title'):")
    for item in field(goods, 'title'):
        print(f"  {item}")

    print("\nfield(goods, 'title', 'price'):")
    for item in field(goods, 'title', 'price'):
        print(f"  {item}")

    print("\nfield(goods, 'price'):")
    for item in field(goods, 'price'):
        print(f"  {item}")

    # Тест с None значениями
    goods_with_none = [
        {'title': 'Стол', 'price': None, 'color': 'white'},
        {'title': None, 'price': None, 'color': None},
        {'title': 'Стул', 'price': 500, 'color': 'brown'}
    ]

    print("\nТест с None значениями:")
    print("field(goods_with_none, 'title'):")
    for item in field(goods_with_none, 'title'):
        print(f"  {item}")

    print("\nfield(goods_with_none, 'title', 'price'):")
    for item in field(goods_with_none, 'title', 'price'):
        print(f"  {item}")