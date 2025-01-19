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
        print("Тесты для задачи E (модуль 3)...")

    def setUp(self):
        self.solution_path = os.path.join("tasks", "module_3", "task_E", "solution.py")

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
            random_string = ""
            my_dict = dict()
            for j in range(3):
                key = "".join(choice(characters) for k in range(6))
                value = "".join(choice(characters) for k in range(6))
                my_dict[key] = value
                if random_string:
                    random_string = random_string + "\n" + key + "\n" + value
                else:
                    random_string = key + "\n" + value
            output_strings = self.run_program_with_input(random_string)
            print(output_strings)
            expected_string = str(my_dict)
            self.assertIn(
                expected_string,
                output_strings,
                msg="В выводе не обнаружен правильный словарь",
            )


if __name__ == "__main__":
    unittest.main()
