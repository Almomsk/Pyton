# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factor(digit):
    prime_number = 2
    lst = []
    while prime_number <= digit:
        if digit % prime_number == 0:
            lst.append(prime_number)
            digit //= prime_number
            prime_number = 2
        else:
            prime_number += 1
    return lst

number = int(input('Введите натуральное число N: '))
print(prime_factor(number))