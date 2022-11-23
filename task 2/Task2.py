# Было:
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_element_odd_position(lst):
#     result = 0
#     for i in range(1, len(lst) - 1, 2):
#         result += lst[i]      
#         print(lst[i])
#     return result


# list1 = [2, 3, 5, 9, 3]
# print(list1)
# print('Элементы списка, стоящие на нечётной позиции: ')
# print(f'Сумма элементов списка, стоящих на нечётной позиции = {sum_element_odd_position(list1)}')

# Стало:

data = [2, 3, 5, 9, 3]
result = sum(data[1::2])
print(result)