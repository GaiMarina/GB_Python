import info_input as info
from datetime import datetime
import csv
from os import path

FILE_NAME = 'phone_book.csv'


def log_input(entry):  # Внес запись в логи в формате csv: дата, время, запись.
    if not path.exists('phone_book.csv'):
        with open(FILE_NAME, 'a', encoding='utf-8') as head_rec:
            head_rec.write(';'.join(['Дата', 'Время', 'Фамилия', 'Имя', 'Отчество', 'Телефон', 'Комментарий' + '\n']))
        head_rec.close()
    with open(FILE_NAME, 'a', encoding='UTF-8') as rec:
        rec.write(f"{datetime.now().strftime('%d.%m.%Y;%H:%M;')}{';'.join(entry)}\n")


def log_import():  # Вывод на консоль.
    with open('phone_book.csv', 'r', newline='') as csv_rec:
        csv_recording = csv.reader(csv_rec)
        for row in csv_recording:
            print(' '.join(row[0].split(';')))
