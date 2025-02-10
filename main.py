import os
import unittest

def discover_and_run_tests(start_dir):
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests

    if total_tests > 0:
        success_rate = (passed_tests / total_tests) * 100
    else:
        success_rate = 0

    print(f"Общее число тестов: {total_tests}")
    print(f"Пройденные тесты: {passed_tests}")
    print(f"Упавшие тесты: {failed_tests}")
    print(f"Уровень прогресса: {success_rate:.2f}%")

if __name__ == "__main__":
    tasks_directory = os.path.join(os.path.dirname(__file__), 'tasks')
    discover_and_run_tests(tasks_directory)