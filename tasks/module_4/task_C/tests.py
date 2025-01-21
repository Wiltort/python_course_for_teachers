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
        print("Тесты для задачи C (модуль 4)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_4", "task_C", "solution.py")

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
        tens = {
            "2": "двадцать",
            "3": "тридцать",
            "4": "сорок",
            "5": "пятьдесят",
            "6": "шестьдесят",
            "7": "семьдесят",
            "8": "восемьдесят",
            "9": "девяносто" 
        }
        ones = {
            "0": "",
            "1": " один",
            "2": " два",
            "3": " три",
            "4": " четыре",
            "5": " пять",
            "6": " шесть",
            "7": " семь",
            "8": " восемь",
            "9": " девять"
        }
        for _ in range(10):
            input_text = f"{randint(20,99)}\n"
            expected_output = tens[input_text[0]] + ones[input_text[1]]
            self.assertEqual(
                self.run_program_with_input(input_text).lower(),
                expected_output,
                msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
