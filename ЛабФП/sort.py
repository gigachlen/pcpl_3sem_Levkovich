"""
Задача 4: Сортировка по модулю в порядке убывания
"""

data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print("=" * 50)
    print("Тестирование сортировки по модулю")
    print("=" * 50)

    print(f"\nИсходные данные: {data}")
    print(f"Ожидаемый результат: [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]")

    # Способ 1: Без использования lambda-функции
    result = sorted(data, key=abs, reverse=True)
    print(f"\n1. Без lambda (key=abs): {result}")

    # Способ 2: С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(f"2. С lambda: {result_with_lambda}")

    # Дополнительная демонстрация
    print("\n" + "-" * 50)
    print("Демонстрация промежуточных вычислений:")
    print("-" * 50)
    for num in sorted(data, key=abs, reverse=True):
        print(f"  {num:>4} -> |{num}| = {abs(num)}")