"""Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат."""


def inputNumbers():
    xyz = ["X", "Y", "Z"]
    temp = []
    for i in range(3):
        temp.append(input(f"Введите значение {xyz[i]}: "))
    return temp


def checkPredicate(temp_list):
    left = not (temp_list[0] or temp_list[1] or temp_list[2])
    right = not temp_list[0] and temp_list[1] and not temp_list[2]
    result = left == right
    return result


if checkPredicate(inputNumbers()):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")