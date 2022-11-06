# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def gen_lst(n): 
    rand_list=[]
    for _ in range(n):
        rand_list.append(random.randint(1, 101))
    return rand_list

def print_poly(poly):
    for i in range(len(poly)):
        print(poly[i], end="")
        if i != 0:
            print("x^", i, end="", sep="")
        if i != len(poly) - 1:
            print("+", end="")


print_poly(gen_lst(3))