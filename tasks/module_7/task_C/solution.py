"""
В файле содержится последовательность натуральных чисел. Её элементы могут принимать целые 
значения от 1 до 100 000 включительно. Определите количество троек последовательности, 
в которых хотя бы один элемент кратен наименьшему числу последовательности, кратному 2025, 
а сумма тройки при этом — шестизначное число.

В ответе запишите количество найденных троек, затем максимальную из сумм элементов таких троек.
В этой задаче под тройкой подразумеваются три идущих подряд элемента последовательности.
"""

# TODO: Напишите свой код ниже

with open("input_data/m7_C.txt") as f:
    numbers = [int(a) for a in f]
Minimum = 100000
for number in numbers:
    if number % 2025 == 0:
        Minimum = min(Minimum, number)
count = 0
Maximum = 0
for i in range(len(numbers) - 2):
    triplet = numbers[i : i + 3]
    Summa = triplet[0] + triplet[1] + triplet[2]
    if (
        triplet[0] % Minimum == 0
        or triplet[1] % Minimum == 0
        or triplet[2] % Minimum == 0
    ) and len(str(Summa)) == 6:
        count += 1
        Maximum = max(Maximum, Summa)
print(count, Maximum)
