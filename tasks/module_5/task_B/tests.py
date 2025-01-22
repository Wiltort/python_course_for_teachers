import sys
import unittest
import os


class TestTaskSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("-" * 70)
        print("Тесты для задачи B (модуль 5)...")
        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "..", "..", "app", "tests"
                )
            )
        )

    def setUp(self):
        self.timeout = 1

    def test_pairs(self):
        """Test with pairs"""
        from timeout import run_with_timeout
        from solution import snake_case

        test_data = {
            'Harry Potter and Germiona': 'harry_potter_and_germiona',
            'For the Glory': 'for_the_glory',
            'ARIA FOREVER': 'aria_forever',
            ' if    You  want': 'if_you_want',
            'aA   hsjA': 'aa_hsja',
            ' are you ready   ': 'are_you_ready',
            'sDj': 'sdj',
            '          sto raz': 'sto_raz'
        }

        for key in test_data:
            result = run_with_timeout(snake_case, self.timeout, key)
            self.assertIsNotNone(result, msg="Время выполнения функции превышено!")
            self.assertEqual(result, test_data[key], msg="Неверный ответ")


if __name__ == "__main__":
    unittest.main()
