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

f = open("input_data/m8_A.txt").readline()
len_pairs = 0
max_len = 0
l = len(f)
 


