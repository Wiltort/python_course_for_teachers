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

def distance(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5


def get_clasters_A(path):
    with open(path) as f:
        f.readline()
        stars = [[float(x.replace(',', '.')) for x in a.split()] for a in f.readlines()]
    l = len(stars)
    min_sum = 10 ** 10
    for i in range(l - 1):
        for j in range(1, l - 1):
            center1 = stars[i]
            center2 = stars[j]
            summ = 0
            for star in stars:
                summ += min(distance(star, center1), distance(star, center2))
            if summ < min_sum:
                min_sum = summ
                res = [center1, center2]
    return int((res[0][0] + res[1][0]) / 2 * 10000), int((res[0][1] + res[1][1]) / 2 * 10000)


def get_center(cluster):
    min_sum = 10**10
    for star in cluster:
        center = star
        summ = 0
        for star in cluster:
            summ += distance(star, center)
        if summ < min_sum:
            min_sum = summ
    return center


def get_clasters_B(path):
    with open(path) as f:
        f.readline()
        stars = [[float(x.replace(',', '.')) for x in a.split()] for a in f.readlines()]
    cluster_1 = list(filter(lambda s: s[0] < 3 and s[1] < 3, stars))
    cluster_2 = list(filter(lambda s: s[0] > 2 and s[0] < 5 and s[1] > 7 and s[1] < 11, stars))
    cluster_3 = list(filter(lambda s: s[0] > 5 and s[0] < 8 and s[1] > 4 and s[1] < 7, stars))
    center_1 = get_center(cluster_1)
    center_2 = get_center(cluster_2)
    center_3 = get_center(cluster_3)
    res = [
        int((center_1[0] + center_2[0] + center_3[0]) / 3 * 10000),
        int((center_1[1] + center_2[1] + center_3[1]) / 3 * 10000)
    ]
    return res

print(*get_clasters_A('input_data/m10_A_A.txt'))
print(*get_clasters_B('input_data/m10_A_B.txt'))
