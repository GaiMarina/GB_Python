import csv
from os import path


def head_line_input():  # дополняем заголовок и отправляем в csv
    column = input("Input the new column name: ")
    if not path.exists('head_line.csv'):
        with open('head_line.csv', 'w') as h:
            h.write(column)
    else:
        with open('head_line.csv', 'a') as h_l:
            h_l.write(';' + column)


def user_input():  # Добавили данные пользователя согласно заголовка и отправили в scv
    with open('head_line.csv', 'r', newline='') as h_l:
        reader = csv.reader(h_l)
        for row in reader:
            head_line = row[0].split(';')
    user_entry = []
    for i in head_line:
        temp = input(f'Input the {i}: ')
        user_entry.append(temp)

    if not path.exists('users_lines.csv'):
        with open('users_lines.csv', 'w') as u_l:
            u_l.write(';'.join(user_entry))  # Маринина;Марина;Сергеевна
            u_l.write('\n')
    else:
        with open('users_lines.csv', 'a') as h_l:
            h_l.write(';'.join(user_entry))
            h_l.write('\n')


def data_export():
    with open('head_line.csv', newline='') as h_l:
        with open('users_lines.csv', newline='') as u_l:
            with open('data_base.csv', 'w') as f:
                reader_1 = csv.reader(h_l)
                reader_2 = csv.reader(u_l)
                writer = csv.writer(f)
                for row in reader_1:
                    writer.writerow(row)
                for row in reader_2:
                    writer.writerow(row)
