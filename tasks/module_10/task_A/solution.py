"""
ФИПИ
Тема: Анализ данных(Анализ данных) https://education.yandex.ru/ege/task/10b197cd-2219-43da-aae1-d88f5ef74cc7

Учёный решил провести кластеризацию некоторого множества звёзд по их расположению на карте
 звёздного неба. Кластер звёзд — это набор звёзд (точек) на графике, лежащий внутри 
 прямоугольника высотой HH и шириной WW. Каждая звезда обязательно принадлежит только одному из кластеров.
Истинный центр кластера, или центроид, — это одна из звёзд на графике, сумма расстояний от которой до всех
 остальных звёзд кластера минимальна.

Под расстоянием понимается расстояние Евклида между двумя точками A(x1,y1)A(x1​,y1​) и B(x2,y2)B(x2​,y2​) на 
плоскости, которое вычисляется по формуле:
d(A,B)=sqrt((x2 —x1)^2+(y2 —y1)^2)

В файле A хранятся данные о звёздах двух кластеров, где H=3, W=3 для каждого кластера.
В каждой строке записана информация о расположении на карте одной звезды: сначала 
координата x, затем координата y. Значения даны в условных единицах. Известно, что 
количество звёзд не превышает 1000.

В файле Б хранятся данные о звёздах трёх кластеров, где H=3, W=3 для каждого кластера. 
Известно, что количество звёзд не превышает 10 000. Структура хранения информации 
о звездах в файле Б аналогична файлу А.

Для каждого файла определите координаты центра каждого кластера, затем вычислите два числа: 
Px — среднее арифметическое абсцисс центров кластеров, и PyPy​ — среднее арифметическое ординат 
центров кластеров.
В ответе запишите четыре числа: в первой строке сначала целую часть произведения Px×10 000, затем 
целую часть произведения Py×10 000 для файла A, во второй строке — аналогичные данные для файла Б.
Для выполнения задания используйте данные из прилагаемых файлов 'input_data/m10_A_A.txt' и
'input_data/m10_A_B.txt'.
"""


# TODO: Напишите свой код ниже

