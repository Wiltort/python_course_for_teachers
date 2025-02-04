"""
 (№ 2924 Д. Поляков) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [113012; 113061], 
 числа, имеющие ровно 4 различных делителя. Выведите для каждого найденного числа два наибольших делителя в порядке возрастания. 
"""


# TODO: Напишите свой код ниже

def get_divisors(n):
    divisors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


for i in range(113012, 113062):
    divs = get_divisors(i)
    if len(divs) == 4:
        print(*sorted(list(divs))[-2:])