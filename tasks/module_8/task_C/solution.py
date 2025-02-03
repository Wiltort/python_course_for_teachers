"""
(№ 2541) (К. Амеличев) Текстовый файл 'input_data/m8_C.txt содержит последовательность
 из символов «(»и «)», всего не более 10^6 символов. Определите, каким по счёту символом
от начала файла окажется 10000-я открывающая скобка «(» (нумерация символов начинается с 1). 
"""


# TODO: Напишите свой код ниже

with open("input_data/m8_C.txt") as f:
    input_string = f.readline()
count = 0
for i in range(len(input_string)):
    if input_string[i] == '(':
        count += 1
        if count == 10000:
            index = i + 1
            break
print(index)
