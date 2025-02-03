"""

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
