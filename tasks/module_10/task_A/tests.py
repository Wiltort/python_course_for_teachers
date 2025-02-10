import sys
import unittest
from io import StringIO
import os


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи A (модуль 10)...")
        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "..", "app", "tests"
                )
            )
        )

    def setUp(self):
        from timeout import run_with_timeout

        self.timeout = 30
        self.solution_path = os.path.join("tasks", "module_10", "task_A", "solution.py")
        self.captured_output = StringIO()
        sys.stdout = self.captured_output
        with open(self.solution_path, "r", encoding="utf-8") as file:
            run_with_timeout(exec, self.timeout, file.read(), globals())

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_right_solution(self):
        """Test with right solution"""
        expected = "10738 30730\n34270 50438\n"
        result = self.captured_output.getvalue()
        self.assertIsNotNone(
            result, msg="Программа не получила верное значение за отведенное время!"
        )
        self.assertEqual(result, expected, msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
