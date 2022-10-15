"""Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
6 -> да
7 -> да
1 -> нет"""

from turtle import clear


def weekend_check(num):
    if 6 == num or num == 7:
        return "ДА"
    else:
        return "НЕТ"


def main():
    flag = True
    while flag:
        number = input("Введите число от 1 до 7: ")
        if number.isdigit():
            number = int(number)
            if 0 <= number > 7:
                print("Ввели не коректное число")
            else:
                print(f"{number} -> {weekend_check(number)}")
                flag = False
        else:
            print("Введино не число. Повторите попытку.")


main()