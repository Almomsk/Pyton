# Было:
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Первому игроку нужно взять количество конфет, равное: candy_count // (max_candy_in_step + 1).

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import *


# print('\nДобро пожаловать в игру с конфетами!\n')

# candy_count = int(input('Введите целое число, обозначающее количество конфет на столе (например: 2021): \n'))
# max_candy_in_step = 28
# count = 0
# player_1 = input('Введите имя первого игрока: \n')
# player_2 = input('Введите имя второго игрока: \n')

# print('\nКто будет ходить первым?\n')

# start = randint(1, 2)
# if start == 1:
#     frst = player_1
#     scnd = player_2
# else: 
#     frst = player_2
#     scnd = player_1 
# print(f'Первым ходит {frst}!')   

# while candy_count > 0:
#     if count == 0:
#         step = int(input(f'{frst} твой ход! Сколько возьмёшь конфет? ',))
#         if step > candy_count or step > max_candy_in_step:
#             if max_candy_in_step < candy_count:
#                 step = int(input(f'{frst} максимальное количество конфет, которое можно взять = {max_candy_in_step}. Введите количество конфет: '))
#             else:
#                 step = int(input(f'{frst} максимальное количество конфет, которое можно взять = {candy_count}. Введите количество конфет: '))
#         candy_count = candy_count - step
#         if candy_count <= 0:
#             print('Игра окончена!')
#         count = 1
#     if count == 1:
#         step = int(input(f'{scnd} твой ход! Сколько возьмёшь конфет? '))
#         if step > candy_count or step > max_candy_in_step:
#             if max_candy_in_step < candy_count:
#                 step = int(input(f'{scnd} максимальное количество конфет, которое можно взять = {max_candy_in_step}. Введите количество конфет: '))
#             else:
#                 step = int(input(f'{scnd} максимальное количество конфет, которое можно взять = {candy_count}. Введите количество конфет: ',))
#         candy_count = candy_count - step
#         if candy_count <= 0:
#             print('Игра окончена!')
#         count = 0


# if count == 0:
#     print(f'{frst} победил(а)')
# if count == 1:
#     print(f'{scnd} победил(а)')

# Стало:
# Использовала функции.

 
from random import *

print('\nДобро пожаловать в игру с конфетами!\n')
candy_count = int(input('Введите целое число, обозначающее количество конфет на столе (например: 2021): \n'))
max_candy_in_step = 28
player_name_1 = input('Введите имя первого игрока: \n')
player_name_2 = input('Введите имя второго игрока: \n')

def step(player_token):
    global candy_count
    step = int(input(f'{player_token} твой ход! Сколько возьмёшь конфет? '))
    if step > candy_count or step > max_candy_in_step:
        if max_candy_in_step < candy_count:
            step = int(input(f'{player_token} максимальное количество конфет, которое можно взять = {max_candy_in_step}. Введите количество конфет: '))
        else:
            step = int(input(f'{player_token} максимальное количество конфет, которое можно взять = {candy_count}. Введите количество конфет: '))
    candy_count = candy_count - step
    return candy_count

def main(player_1, player_2):
    count = 0
    print('\nКто будет ходить первым?\n')
    start = randint(1,2)
    if start == 1:
        frst = player_1
        scnd = player_2
    else: 
        frst = player_2
        scnd = player_1 
    print(f'Первым ходит {frst}!') 
    
    while candy_count > 0: 
        if count % 2 == 0:
            step(frst)
        else:
            step(scnd)  
        if candy_count > 0:    
            count += 1
        else:
            print('Игра окончена!')
            break

    if candy_count == 0:
        if count % 2 == 0:
            print(f'{frst} победил(а)')
        else:
            print(f'{scnd} победил(а)')
   

main(player_name_1, player_name_2)