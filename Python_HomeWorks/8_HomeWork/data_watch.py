import csv

import openpyxl


def database_import():  # Вывод на консоль.
    with open('data_base.csv', newline='') as csv_rec:
        reader = csv.reader(csv_rec)
        for row in reader:
            print(' '.join(row[0].split(';')))


def csv_to_excel():
    wb = openpyxl.Workbook()
    ws = wb.active

    with open('data_base.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            ws.append(row)

    wb.save('data_base.xlsx')
