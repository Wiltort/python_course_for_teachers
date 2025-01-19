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
        print("Тесты для задачи B (модуль 3)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_3", "task_B", "solution.py")

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

    def test_5_53(self):
        """Test with numbers 1, 2, 3"""
        input_text = "5\n53"
        expected_output = "10"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_zero(self):
        """Test with zero"""
        input_text = "3\n0"
        expected_output = "0"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_random_10(self):
        """Test with random numbers"""
        for _ in range(10):
            price = randint(1, 1000)
            cash = randint(1, 2000)
            input_text = f"{price}\n{cash}"
            expected_output = str(cash // price)
            self.assertEqual(self.run_program_with_input(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()
