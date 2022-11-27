# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = 'AAAABBBBNNNNMMMMLLLLLLLLL'

set_text = set(text) #{'A', 'L', 'N', 'M', 'B'}
counter = 0 
for i in set_text:
    for j in text:
        if i == j:
            counter += 1

    dict_text = [i, counter]
    print(dict_text)