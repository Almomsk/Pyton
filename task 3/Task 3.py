# Было:
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Доброе абвгд утро! абв Сегодня абвгд будет замечательный ааабв день.'

# words = text.split(' ')
# result = []
# for word in words:
#     if 'абв' not in word:
#         result.append(word)
# result = ' '.join(result)

# print(result)

test_list = text.split()

print(" ". join(filter(lambda word: "абв" not in word, test_list)))