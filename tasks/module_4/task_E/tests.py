import sys
import unittest
from io import StringIO
import os
from contextlib import contextmanager
from unittest.mock import patch
from random import choice, randint
import string


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи E (модуль 4)...")
        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "..", "app", "tests"
                )
            )
        )

    def setUp(self):
        self.timeout = 1
        self.solution_path = os.path.join("tasks", "module_4", "task_E", "solution.py")

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
        """Test with 10 random strings"""
        from timeout import run_with_timeout

        characters = string.ascii_lowercase
        n = 2000
        for _ in range(10):
            random_string = "".join(choice(characters) for i in range(n))
            i = randint(0, n)
            letter = choice(characters)
            second_string = random_string[:i] + letter + random_string[i:]
            input_string = random_string + "\n" + second_string
            result = run_with_timeout(
                self.run_program_with_input, self.timeout, input_string
            )
            self.assertIsNotNone(result, msg="Время выполнения функции превышено!")
            self.assertEqual(result, letter, msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
