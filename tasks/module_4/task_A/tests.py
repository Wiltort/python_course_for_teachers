import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch
from random import randint


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи A (модуль 4)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_4", "task_A", "solution.py")

    @contextmanager
    def _run_with_input(self, input_text):
        """Context manager to safely handle file operations and IO mocking"""
        with open(self.solution_path, encoding='utf-8') as solution_file:
            solution_code = solution_file.read()
            with patch('sys.stdin', StringIO(input_text)), \
                 patch('sys.stdout', new=StringIO()) as fake_output:
                exec(solution_code)
                yield fake_output.getvalue().strip()

    def run_program_with_input(self, input_text):
        """Helper method to run the program with specific input"""
        with self._run_with_input(input_text) as output:
            return output

    def test_random_10(self):
        """Test with 10 random numbers"""
        for _ in range(10):
            input_text = f"{str(randint(1,100))}\n"
            expected_output = "четное" if int(input_text) % 2 == 0 else "нечетное"
            self.assertEqual(
                self.run_program_with_input(input_text).lower(),
                expected_output,
                msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
