"""
Текстовый файл состоит из символов A, B и C.
Определите максимальное количество идущих подряд пар символов AB
или CB в прилагаемом файле.
Искомая подпоследовательность должна состоять только из пар AB, или 
только из пар CB, или только из пар AB и CB в произвольном порядке
следования этих пар.

Для выполнения этого задания следует написать программу.
"""


# TODO: Напишите свой код ниже

with open("input_data/m8_A.txt") as f:
    input_string = f.readline()
input_string = input_string.replace('AB', 'x')
input_string = input_string.replace('CB', 'x')
word_len = 0
max_word_len = 0
for char in input_string:
    if char == 'x':
        word_len += 1
    else:
        max_word_len = max(word_len, max_word_len)
        word_len = 0
max_word_len = max(word_len, max_word_len)
print(max_word_len)
