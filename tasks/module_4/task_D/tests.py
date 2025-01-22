import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch
from random import choice
import string


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи D (модуль 4)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_4", "task_D", "solution.py")

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
        """Test with 10 random strings"""
        characters = string.ascii_letters + string.digits + " "
        for _ in range(10):
            random_string = "".join(choice(characters) for i in range(20))
            right_dict = dict()
            for char in random_string:
                letter = char.lower()
                if letter in right_dict:
                    right_dict[letter] += 1
                else:
                    right_dict[letter] = 1
            self.assertEqual(
                eval(self.run_program_with_input(random_string)),
                right_dict,
                msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
