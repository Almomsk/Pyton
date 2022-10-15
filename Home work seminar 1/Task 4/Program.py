"""Напишите программу, которая по заданному номеру четверти, показывает диапазон
 возможных координат точек в этой четверти (x и y)."""



def is_number(temp):
    try:
        float(temp)
        return True
    except ValueError:
        return False

def main():
    flag = True
    while flag:
        number = input('Введите номер четверти: ')
        if is_number(number):
            number = int(number)
            if number > 0 and number <= 4:
                if number == 1:
                    print('x > 0 and y > 0')
                elif number == 2:
                    print('x < 0 and y > 0')
                elif number == 3:
                    print('x < 0 and y < 0')
                elif number == 4:
                    print('x > 0 and y < 0')
                break
            else:
                print("Число должно быть в диапазоне от 1 до 4")
        else:
            print("Ввели не число")
        

     
main()