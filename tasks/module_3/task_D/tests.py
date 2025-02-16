import unittest
from io import StringIO
import sys
import os


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи D (модуль 3)...")

    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

        # Import the solution script
        self.solution_path = os.path.join("tasks", "module_3", "task_D", "solution.py")
        with open(self.solution_path, "r") as file:
            exec(file.read(), globals())

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_vars(self):
        # Проверяем наличие нужных переменных в программе
        self.assertIn(
            "my_list", globals(), "Переменная my_list отсутствует в solution.py"
        )
        self.assertIn(
            "other_list", globals(), "Переменная other_list отсутствует в solution.py"
        )

    def test_my_list_length(self):
        # Проверяем, что длина списка my_list равна 6
        try:
            self.assertEqual(
                len(my_list),
                6,
                msg="После выполнения программы длина списка my_list должна быть равна 6!",
            )
        except NameError:
            self.assertTrue(False, msg='my_list не найден')

    def test_my_list_content(self):
        # Проверяем, что список my_list содержит разнотипные элементы
        try:
            types = {type(item) for item in my_list[:4]}
            self.assertGreater(
                len(types), 3, msg="my_list должен состоять из разнотипных элементов!"
            )
        except NameError:
            self.assertTrue(False, msg='my_list не найден!')

    def test_console_output(self):
        # Проверяем правильность вывода в терминал
        # Check if '4' is in the output
        self.assertIn(
            "4\n",
            self.captured_output.getvalue(),
            msg="В терминале отсутствует вывод верного ответа на вопрос 3!",
        )


if __name__ == "__main__":
    unittest.main()
