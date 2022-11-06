# Вычислить число π c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

def input_natural(text):
    n_str = input(text)
    while not n_str.isdigit():
        n_str = input(f'{text}')
        return int(n_str)

def get_pi_nilacant(d):
    pi_s = 0
    pi_n = 3
    sign = 1
    n = 2
    while abs(pi_s-pi_n) > 10**(-10):
        pi_s = pi_n
        pi_n += sign * 4 / (n * (n + 1) * (n + 2))
        n += 2
        sign = - sign
    return pi_n


d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'Число π = {math.pi} с точностью до {d} знаков после запятой равно {get_pi_nilacant(d)}')

