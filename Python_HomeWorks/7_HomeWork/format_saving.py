import csv
import pandas as pd
import openpyxl
from os import path


def html_exp():
    if path.exists('phone_book.csv'):
        read_rec = pd.read_csv('phone_book.csv', delimiter=';')
        read_rec.to_html('phone_book.html')
        html_rec = read_rec.to_html()
    with open('phone_book.html', 'w', encoding='utf-8') as write_rec:
        write_rec.write('<!DOCTYPE html><html><head><title>Обучение</title><meta charset="utf-8" /></head><body>')
        write_rec.write(html_rec)
        write_rec.write('</body></html>')


def csv_to_excel():
    wb = openpyxl.Workbook()
    ws = wb.active

    with open('phone_book.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            ws.append(row)

    wb.save('phone_book.xlsx')
