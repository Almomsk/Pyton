"""Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
x=34; y=-30 -> 4
x=2; y=4-> 1
x=-34; y=-30 -> 3"""



coordinates = {'x': None, 'y': None}

def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False

def checkCoordinates(xy):
    number = 4
    if xy['x'] > 0 and xy['y'] > 0:
        number = 1
    elif xy['x'] < 0 and xy['y'] > 0:
        number = 2
    elif xy['x'] < 0 and xy['y'] < 0:
        number = 3
    print(f"x = {xy['x']}; y = {xy['y']} -> {number} ")

def main(coord):
    flag = True
    for elem in coord.keys():
        while flag:
            number = input(f"Введите число для {elem}: ")
            if is_number(number):
                if int(number) != 0:
                    if coord['x'] == None:
                        coord['x'] = int(number)
                        break
                    elif coord['x'] != None and coord['y'] == None:
                        coord['y'] = int(number)
                        flag = False
                else:
                    print('Координата не должна быть равна 0.')
            else:
                print("Введино не число. Повторите попытку.")
    checkCoordinates(coord)



main(coordinates)