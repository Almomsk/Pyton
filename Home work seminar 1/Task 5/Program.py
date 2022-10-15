"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между
 ними в 2D пространстве.
Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21
"""


def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False

def inputNumber():
    ab = ['A', 'B']
    xy = ['X', 'Y']
    flag = True
    coord = {'ax': None, 'ay': None, 'bx': None, 'by': None}
    for elem in ab:
        print(f"Введите координаты точки {elem}")
        for _elem in xy:
            while flag:
                num_temp = input(f"Введите координаты по {_elem}: ")
                if is_number(num_temp):
                    if coord['ax'] == None and coord['ay'] == None and coord['bx'] == None and coord['by'] == None:
                        coord['ax'] = int(num_temp)
                        break
                    elif coord['ax'] != None and coord['ay'] == None and coord['bx'] == None and coord['by'] == None:
                        coord['ay'] = int(num_temp)
                        break
                    elif coord['ax'] != None and coord['ay'] != None and coord['bx'] == None and coord['by'] == None:
                        coord['bx'] = int(num_temp)
                        break
                    elif coord['ax'] != None and coord['ay'] != None and coord['bx'] != None and coord['by'] == None:
                        coord['by'] = int(num_temp)
                        flag = False
                else:
                    print("Введино не число. Повторите попытку.")
    return coord

def findDistance(coord_temp):
    summa = round((((coord_temp['bx'] - coord_temp['ax']) ** 2 + (coord_temp['by'] - coord_temp['ay']) ** 2) ** (0.5) ), 2)
    print(f" A ({coord_temp['ax']}, {coord_temp['ay']}); B ({coord_temp['bx']}, {coord_temp['by']}) -> {summa}")
   
coordinates = inputNumber()
findDistance(coordinates)