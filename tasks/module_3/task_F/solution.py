"""
Даны два множества first_set и second_set
1. Добавьте в first_set ещё один элемент
2. Найдите общие элементы в двух множествах и поместите их в новое
   множество third_set
3. Конвертируйте third_set в список и сохраните как my_list
4. Выведите в терминал third_set
5. Выведите в терминал my_list
"""

first_set = {2, 8, 6, 12, 11}
second_set = {5, 6, 7, 8, 11}

# TODO: Напишите свой код ниже
first_set.add(4)
third_set = first_set.intersection(second_set)
my_list = list(third_set)
print(third_set)
print(my_list)
