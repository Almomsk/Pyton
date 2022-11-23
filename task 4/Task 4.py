# Было:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#text = 'AAAABBBBNNNNMMMMLLLLLLLLL'

# set_text = set(text) #{'A', 'L', 'N', 'M', 'B'}
# counter = 0 
# for i in set_text:
#     for j in text:
#         if i == j:
#             counter += 1

#     dict_text = [i, counter]
#     print(dict_text)

# Стало (не было модуля восстановления данных):

def coding(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")