#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.



with open('poly_1.txt', 'w') as file:
    file.write('4 + 2x^1 + 3x^2')
  
with open('poly_2.txt', 'w') as file:
    file.write('2 + 3x^1 + 2x^2')

def convert_pol(pol):  
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    return pol

def print_poly(poly):
    for i in range(len(poly)):
        print(poly[i], end="")
        if i != 0:
            print("x^", i, end="", sep="")
        if i != len(poly) - 1:
            print("+", end="")

print(p1)
print(p2)
print()
print(convert_pol(p1))
print(convert_pol(p2))
pol1_coef = list(map(int, convert_pol(p1)))
pol2_coef = list(map(int, convert_pol(p2)))
print(pol1_coef)
print(pol2_coef)
print()



pol3_coef = list(map(sum, zip(pol1_coef, pol2_coef)))
print(pol3_coef)
print()
res = str(print_poly(pol3_coef))
print(res)

with open('poly_3.txt', 'w') as file:
    file.write(f'{res}=0')
