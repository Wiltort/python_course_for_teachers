"""
 	(№ 4947 Д. Поляков) Особыми будем называть нетривиальные делители числа, все цифры 
    которых нечётные. Нетривиальными считаются все делители, кроме 1 и самого числа. 
    Пусть D(N) – пятый по величине (считая с наибольшего) особый делитель натурального 
    числа N. Если у числа N меньше пяти различных особых делителей, то принимаем D(N) = 0. 
    Найдите 5 наибольших натуральных чисел, меньших 300 000 000, для которых D(N) > 0. 
    В ответе запишите для каждого найденного N сначала значение D(N), а затем общее количество 
    особых делителей (в порядке возрастания соответствующих чисел N). 
"""

# TODO: Напишите свой код ниже

def is_special(n):
    for char in str(n):
        if char in {'0', '2', '4', '6', '8'}:
            return False
    return True


def d(n):
    specials = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            x = n // i
            if is_special(x):
                specials.append(x)
            if is_special(i) and x != i:
                specials.append(i)
    if len(specials) < 5:
        return 0, len(specials)
    return sorted(specials)[-5], len(specials)

count = 0
results = []
for i in range(299999999, 1, -1):
    value, num = d(i)
    if value > 0:
        count += 1
        results.append((value, num))
        if count == 5:
            break
for item in results[::-1]:
        print(*item)