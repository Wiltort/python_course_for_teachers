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
        print("Тесты для задачи B (модуль 4)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_3", "task_A", "solution.py")

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
            input_text = f"{str(randint(100,1000000))}\n"
            expected_output = "да" if input_text[0] == input_text[-1] else "нет"
            self.assertIn(
                self.run_program_with_input(input_text).lower(),
                expected_output,
                msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
