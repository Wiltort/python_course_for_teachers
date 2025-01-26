"""
В файле содержится последовательность натуральных чисел, каждое из которых 
не превышает 100 000. Определите количество троек элементов последовательности,
в которых ровно два из трёх элементов являются трёхзначными числами, а сумма
элементов тройки не больше максимального элемента последовательности, оканчивающегося на 13.
Гарантируется, что в последовательности есть хотя бы одно число, оканчивающееся на 13.
В ответе запишите количество найденных троек чисел, затем максимальную из сумм
элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд
элемента последовательности.
"""


# TODO: Напишите свой код ниже
def get_number_of_equal_in_length_items(number_list, length):
    count = 0
    for number in number_list:
        if len(str(number)) == length:
            count += 1
    return count


with open("input_data/m7_E.txt") as f:
    numbers = [int(a) for a in f]
max_item_13 = 0
for number in numbers:
    if str(number)[-2:] == "13":
        max_item_13 = max(max_item_13, number)
count = 0
maximum = 0
for i in range(len(numbers) - 2):
    triplet = numbers[i:i + 3]
    Summa = triplet[0] + triplet[1] + triplet[2]
    if get_number_of_equal_in_length_items(triplet, 3) == 2 and Summa <= max_item_13:
        count += 1
        maximum = max(maximum, Summa)
print(count, maximum)
