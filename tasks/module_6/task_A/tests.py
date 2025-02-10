import sys
import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи A (модуль 6)...")
        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "..", "app", "tests"
                )
            )
        )

    def setUp(self):
        self.timeout = 1
        self.solution_path = os.path.join("tasks", "module_6", "task_A", "solution.py")

    @contextmanager
    def _run_with_input(self, input_text):
        """Context manager to safely handle file operations and IO mocking"""
        with open(self.solution_path, encoding="utf-8") as solution_file:
            solution_code = solution_file.read()
            with patch("sys.stdin", StringIO(input_text)), patch(
                "sys.stdout", new=StringIO()
            ) as fake_output:
                exec(solution_code)
                yield fake_output.getvalue().strip()

    def run_program_with_input(self, input_text):
        """Helper method to run the program with specific input"""
        with self._run_with_input(input_text) as output:
            return output

    def test_with_dataset(self):
        """Test with dataset"""
        from timeout import run_with_timeout

        test_data = [
            {"input": "2\n5\n8\n", "output": 5},
            {"input": "3\n10\n25\n15\n", "output": 25},
            {"input": "3\n15\n20\n10\n", "output": 20},
        ]
        for item in test_data:
            result = run_with_timeout(
                self.run_program_with_input, self.timeout, item["input"]
            )
            self.assertIsNotNone(result, msg="Время выполнения функции превышено!")
            self.assertEqual(result, str(item["output"]), msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
