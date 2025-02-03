"""
 	(№ 4947 Д. Поляков) Особыми будем называть нетривиальные делители числа, все цифры 
    которых нечётные. Нетривиальными считаются все делители, кроме 1 и самого числа. 
    Пусть D(N) – пятый по величине (считая с наибольшего) особый делитель натурального 
    числа N. Если у числа N меньше пяти различных особых делителей, то принимаем D(N) = 0. 
    Найдите 5 наибольших натуральных чисел, меньших 300 000 000, для которых D(N) > 0. 
    В ответе запишите для каждого найденного N сначала значение D(N), а затем общее количество 
    особых делителей (в порядке возрастания соответствующих чисел N). 
"""
"""
# TODO: Напишите свой код ниже

from math import sqrt, ceil
def is_special(n):
    for char in str(n):
        if char in ['0', '2', '4', '6', '8']:
            return False
    return True


def d(n):
    divisor = 2
    specials_right = []
    specials_left = []
    for i in range(2, ceil(sqrt(n))):
        if n % divisor == 0:
            x = n / divisor
            if is_special(x):
                specials_right.append(x)
            if is_special(divisor):
                specials_left.append(divisor)
            divisor += 1
    specials = specials_left + specials_right
    if len(specials) < 5:
        return 0, len(specials)
    return specials[-5], len(specials)


count = 0
for i in range(300000000, 1, -1):
    value, num = d(i)
    if value > 0:
        count += 1
        print(value, num, i)
        if count == 5:
            break
"""
def is_odd_digit(digit):
    return digit in {'1', '3', '5', '7', '9'}

def has_only_odd_digits(number):
    return all(is_odd_digit(d) for d in str(number))

def find_special_divisors(n):
    special_divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if has_only_odd_digits(i):
                special_divisors.append(i)
            if i != n // i and has_only_odd_digits(n // i):
                special_divisors.append(n // i)
    return special_divisors

def find_top_5_numbers(limit):
    results = []
    for n in range(limit - 1, 1, -1):
        special_divisors = find_special_divisors(n)
        special_divisors.sort(reverse=True)
        if len(special_divisors) >= 5:
            D_n = special_divisors[4]
            results.append((n, D_n, len(special_divisors)))
            if len(results) == 5:
                break
    return sorted(results)

if __name__ == "__main__":
    limit = 300_000_000
    top_5_numbers = find_top_5_numbers(limit)
    for n, D_n, count in top_5_numbers:
        print(f"N: {n}, D(N): {D_n}, Count: {count}")