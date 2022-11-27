def get_menu_value():
    print('''Выберите пункт меню:
    1 - Просмотреть базу
    2 - Добавить запись в базу
    3 - Найти/изменить запись в базе
    4 - Удалить запись в базе
    5 - Сохранить данные в файл
    X - Выход''')
    return input('--> : ').lower()


def view_data(data):
    print(data)


def get_file_name():
    return input('Введите название файла: ')


def get_new_data(col_name):
    return input(col_name)


def get_id_info():
    return input('Введите ID записи: ')