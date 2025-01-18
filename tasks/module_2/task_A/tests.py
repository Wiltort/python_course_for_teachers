import unittest
from io import StringIO
import sys
import os


class TestTaskASolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи А (модуль 2)...")

    @classmethod
    def tearDownClass(cls):
        print("Все тесты успешно пройдены!")

    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

        # Import the solution script
        self.solution_path = os.path.join("tasks", "module_2", "task_A", "solution.py")
        with open(self.solution_path, "r") as file:
            exec(file.read(), globals())

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()