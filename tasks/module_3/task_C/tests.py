import unittest
from io import StringIO
import os
import string
from contextlib import contextmanager
from unittest.mock import patch
from random import choice


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи С (модуль 3)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_3", "task_C", "solution.py")

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

    def test_random_10(self):
        """Test with random strings (len = 6)"""
        characters = string.ascii_letters + string.digits + " "
        for _ in range(10):
            random_string = "".join(choice(characters) for k in range(6))
            output_strings = [
                a for a in self.run_program_with_input(random_string).splitlines()
            ]
            expected_strings = [
                random_string[0],
                random_string[-1],
                str(len(random_string)),
                random_string[1:4],
                str(random_string.count(' ')),
                random_string.replace(' ', '')
            ]
            try:
                for i in range(6):
                    self.assertEqual(
                        output_strings[i],
                        expected_strings[i],
                        msg=f'Неверный ответ на вопрос №{i + 1}'
                    )
            except IndexError:
                self.assertTrue(False, msg='отсутсвуют верные ответы!')


if __name__ == "__main__":
    unittest.main()
