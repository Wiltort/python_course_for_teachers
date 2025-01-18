import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch
from random import randint, sample


class TestTaskASolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи B (модуль 2)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_2", "task_B", "solution.py")

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

    def test_numbers123(self):
        """Test with numbers 1, 2, 3"""
        input_text = "1\n2\n3"
        expected_output = str(6)
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_zero(self):
        """Test with zero"""
        input_text = "2\n0\n3"
        expected_output = "0"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_random(self):
        """Test with random numbers"""
        numbers = sample(range(0, 1001), 3)
        input_text = '\n'.join(map(str, numbers))
        expected_output = str(numbers[0]*numbers[1]*numbers[2])
        self.assertEqual(self.run_program_with_input(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()
