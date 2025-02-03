"""
(№ 6651) (Е. Джобс) Текстовый файл 'input_data/m8_B.txt' состоит не более чем из 
10^6 символов и содержит только заглавные буквы латинского 
алфавита. Определите минимальную длину подстроки, в которой ровно 
три тройки BAD или FAT. Например, в строке 
SDFATFDBADZZSFATBADGHTBAD есть три подходящие подстроки FATFDBADZZSFAT,
 BADZZSFATBAD и FATBADGHTBAD. Минимальная длина 12. 
"""


# TODO: Напишите свой код ниже

with open("input_data/m8_B.txt") as f:
    input_string = f.readline()
min_len = 10 ** 6
input_string = input_string.replace('BAD', 'x')
input_string = input_string.replace('FAT', 'x')
indexes = []
for i in range(len(input_string)):
    if input_string[i] == 'x':
        indexes.append(i)
        if len(indexes) > 2:
            min_len = min(min_len, i - indexes[-3] + 7)
print(min_len)
