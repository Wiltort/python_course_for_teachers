"""
Напишите программу для решения следующей задачи. Камера наблюдения 
регистрирует в автоматическом режиме скорость проезжающих мимо нее 
автомобилей, округляя значения скорости до целых чисел. Необходимо 
определить минимальную зарегистрированную скорость автомобиля. Если 
скорость хотя бы одного автомобиля была больше 80 км/ч, выведите 
«YES», иначе выведите «NO».

Программа получает на вход число проехавших автомобилей N (1 ≤ N ≤ 30), 
затем указываются их скорости. Значение скорости не может быть меньше 1 
и больше 300.Программа должна сначала вывести минимальную скорость, затем YES или NO. 
Пример работы программы:
Входные данные:
4
74
69
63
96
Выходные данные: 
63
YES
"""

# TODO: Напишите свой код ниже
N = int(input())
min_speed = 301
overspeed = 'NO'
for i in range(N):
    speed = int(input())
    min_speed = min(speed, min_speed)
    if speed > 80:
        overspeed = 'YES'
print(min_speed)
print(overspeed)