import csv

import controller
import interface


def menu_choice(data):
    if data == '1':
        view_file_csv()
    elif data == '2':
        add_row_in_file_csv()
    elif data == '3':
        change_row_in_file_csv()
    elif data == '4':
        delete_row_in_file_csv()
    elif data == '5':
        create_file_csv()
    elif data == 'x':
        exit()
    else:
        print('Выбрано не верное значения, повторите ввод!')
        controller.run()


def create_file_csv():
    with open(f'{interface.get_file_name()}', 'w', encoding='utf-8') as file:
        fieldnames = ['id', 'Имя', 'Фамилия', 'Дата рождения', 'Место проживания', 'Телефон']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


def view_file_csv():
    with open('db.csv', 'r', newline='', encoding='utf-8') as file:
        for data in csv.reader(file):
            interface.view_data(data)


def add_row_in_file_csv():
    with open('db.csv', 'r+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        row = next(reader)
        data = [interface.get_new_data(f'{row[0]}: '), interface.get_new_data(f'{row[1]}: '),
                interface.get_new_data(f'{row[2]}: '), interface.get_new_data(f'{row[3]}: '),
                interface.get_new_data(f'{row[4]}: '), interface.get_new_data(f'{row[5]}: ')]
        writer = csv.writer(file)
        writer.writerow(data)


def change_row_in_file_csv():
    id_data = interface.get_id_info()
    file = open('db.csv', 'r')
    new_file = open('db.csv', 'r+')
    writer = csv.writer(new_file)
    for row in csv.reader(file):
        if row[0] == id_data:
            print(f'Найдена запись:{row}\nИзменить запись: ', end='')
            data = input().split(',')
            writer.writerow(data)
            continue
        writer.writerow(row)
    file.close()
    new_file.close()


def delete_row_in_file_csv():
    id_data = interface.get_id_info()
    file = open('db.csv', 'r')
    new_file = open('db.csv', 'r+')
    writer = csv.writer(new_file)
    for row in csv.reader(file):
        if row[0] == id_data:
            print(f'Найдена запись:{row}\nЗапись удалена!')
            continue
        writer.writerow(row)
    file = open('db.csv', 'w+')
    file.close()
    new_file.close()