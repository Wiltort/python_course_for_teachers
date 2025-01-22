import sys
import unittest
import os
from random import randint


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи A (модуль 5)...")
        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "..", "app", "tests"
                )
            )
        )

    def setUp(self):
        self.timeout = 1

    def test_random_10(self):
        """Test with 10 random pairs"""
        from timeout import run_with_timeout
        from solution import rectangle_area

        for _ in range(10):
            pair = [randint(1, 10000) for i in range(2)]
            area = pair[0] * pair[1]
            result = run_with_timeout(rectangle_area, self.timeout, *pair)
            self.assertIsNotNone(result, msg="Время выполнения функции превышено!")
            self.assertEqual(result, area, msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
