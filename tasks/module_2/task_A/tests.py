import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch


class TestTaskASolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи А (модуль 2)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_2", "task_A", "solution.py")

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

    def test_basic_strings(self):
        """Test with basic string inputs"""
        input_text = "Hello\nWorld"
        expected_output = "Hello\nWorld"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_numbers_as_strings(self):
        """Test with numbers as string input"""
        input_text = "42\n123"
        expected_output = "42\n123"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_special_characters(self):
        """Test with special characters"""
        input_text = "!@#$%\n&*()"
        expected_output = "!@#$%\n&*()"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_cyrillic_characters(self):
        """Test with Cyrillic characters"""
        input_text = "Привет\nМир"
        expected_output = "Привет\nМир"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)

    def test_spaces(self):
        """Test with strings containing spaces"""
        input_text = "Hello World\nGoodbye World"
        expected_output = "Hello World\nGoodbye World"
        self.assertEqual(self.run_program_with_input(input_text), expected_output)


if __name__ == "__main__":
    unittest.main()
