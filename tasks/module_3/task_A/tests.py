import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи A (модуль 3)...")

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

    def test_latin(self):
        """Test with latin chars"""
        input_text = "Anna\n18"
        expected_output = "Вас зовут Anna. Ваш возраст: 18!"
        self.assertIn(self.run_program_with_input(input_text), expected_output)

    def test_cyrillic(self):
        """Test with cyrillic chars"""
        input_text = "Дима\n50"
        expected_output = "Вас зовут Дима. Ваш возраст: 50!"
        self.assertIn(self.run_program_with_input(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()
