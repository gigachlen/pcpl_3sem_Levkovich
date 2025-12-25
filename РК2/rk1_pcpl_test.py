import unittest

from rk1_pcpl_refactored import (
    DataRow,
    DataTable,
    RowTableLink,
    query1_rows_with_tables,
    query2_tables_with_row_counts,
    query3_rows_ending_with_ov_mm,
)


class TestRK1Queries(unittest.TestCase):
    def setUp(self) -> None:
        # Минимально понятные тестовые данные
        self.tables = [
            DataTable(1, "Пользователи"),
            DataTable(2, "Заказы"),
            DataTable(3, "Логи"),
        ]
        self.rows = [
            DataRow(1, "Иванов", 6, 1),
            DataRow(2, "Петров", 6, 1),
            DataRow(3, "Заказ #1024", 10, 2),
            DataRow(4, "Событие: вход", 13, 3),
            DataRow(5, "Сидоров", 7, 1),
        ]
        self.links = [
            RowTableLink(1, 1),
            RowTableLink(1, 3),
            RowTableLink(2, 1),
            RowTableLink(3, 2),
            RowTableLink(4, 3),
            RowTableLink(5, 1),
            RowTableLink(5, 2),
        ]

    def test_query1_sorted_by_row_text(self) -> None:
        """
        Запрос 1 должен сортировать по тексту строки (по возрастанию).
        Проверяем только порядок text, не привязываясь к конкретной сортировке таблиц.
        """
        result = query1_rows_with_tables(self.rows, self.tables)
        texts = [t for t, _ in result]
        self.assertEqual(texts, sorted(texts, key=str.lower))

    def test_query2_counts_and_sorting(self) -> None:
        """
        Запрос 2:
        Пользователи: 3 строки (table_id=1)
        Заказы: 1 строка (table_id=2)
        Логи: 1 строка (table_id=3)
        Отсортировано по количеству: 1, 1, 3
        """
        result = query2_tables_with_row_counts(self.rows, self.tables)
        self.assertEqual(result, [("Заказы", 1), ("Логи", 1), ("Пользователи", 3)])

    def test_query3_endswith_ov_mm(self) -> None:
        """
        Запрос 3 (М—М):
        Должны попасть строки на "ов": Иванов, Петров, Сидоров
        И пары по links:
        Иванов: Пользователи, Логи
        Петров: Пользователи
        Сидоров: Пользователи, Заказы
        """
        result = query3_rows_ending_with_ov_mm(self.rows, self.tables, self.links)
        expected = [
            ("Иванов", "Логи"),
            ("Иванов", "Пользователи"),
            ("Петров", "Пользователи"),
            ("Сидоров", "Заказы"),
            ("Сидоров", "Пользователи"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()