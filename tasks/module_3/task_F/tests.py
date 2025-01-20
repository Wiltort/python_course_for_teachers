import unittest
from io import StringIO
import sys
import os


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи F (модуль 3)...")

    def setUp(self):
        # Redirect stdout to capture print statements
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

        # Import the solution script
        self.solution_path = os.path.join("tasks", "module_3", "task_F", "solution.py")
        with open(self.solution_path, "r") as file:
            exec(file.read(), globals())

    def tearDown(self):
        # Reset redirect.
        sys.stdout = sys.__stdout__

    def test_vars(self):
        # Проверяем наличие нужных переменных в программе
        vars = ["first_set", "second_set", "third_set", "my_list"]
        for var in vars:
            self.assertIn(
                var, globals(), f"Переменная {var} отсутствует в solution.py"
            )

    def test_one(self):
        # Проверяем первый пункт
        self.assertEqual(
            len(first_set),
            6,
            msg="После выполнения программы длина множества first_set должна быть равна 6!",
        )
        self.assertTrue(
            {2, 8, 6, 12, 11}.issubset(first_set),
            msg='начальные значения отсутствут в измененном first_set!')
        

    def test_two(self):
        # Проверяем второй пункт
        expected_set = first_set.intersection(second_set)
        self.assertEqual(
            third_set,
            expected_set,
            msg="Второе задание неверно!"
        )
    
    def test_three(self):
        # Проверяем второй пункт
        expected_list = list(third_set)
        self.assertEqual(
            my_list,
            expected_list,
            msg="Третье задание неверно!"
        )

    def test_console_output(self):
        # Проверяем правильность вывода в терминал
        self.assertIn(
            str(third_set),
            self.captured_output.getvalue(),
            msg="В терминале отсутствует third_set (пункт 4)!",
        )
        self.assertIn(
            str(list(third_set)),
            self.captured_output.getvalue(),
            msg="В терминале отсутствует my_list (пункт 5)!",
        )


if __name__ == "__main__":
    unittest.main()
