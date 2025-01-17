# python_course_for_teachers
Задачи для курса


Добро пожаловать на курс Python для учителей! Этот репозиторий содержит задачи для участников курса, рассортированные по папкам с уроками. Каждая папка урока содержит задачи, которые необходимо решить, и тесты для проверки решений.

## Структура проекта

Проект организован по урокам, и каждый урок имеет свою папку. В каждой папке урока находятся несколько задач, каждая из которых представлена двумя файлами:

- `solution.py`: файл, в который участники должны записать свое решение задачи.
- `tests.py`: файл с тестами, которые проверяют правильность решения.

### Пример структуры папок
python_course_for_teachers/<br> │<br> ├── lesson_1/<br> │ ├── task_A/ │ │ ├── solution.py │ │ └── tests.py │ ├── task_B/ │ │ ├── solution.py │ │ └── tests.py │ └── ... │ ├── lesson_2/ │ ├── task_A/ │ │ ├── solution.py │ │ └── tests.py │ └── ... │ └── ...


## Инструкции по решению задач

1. Перейдите в папку с задачей, которую вы хотите решить (например, `lesson_1/task_A`).
2. Откройте файл `solution.py` и напишите свое решение.
3. Сохраните изменения в файле `solution.py`.

## Инструкции по тестированию решений

1. Убедитесь, что вы находитесь в корневой папке проекта.
2. Запустите тесты для задачи, используя команду:
   ```bash
   python -m unittest discover -s lesson_X/task_Y -p 'tests.py'
