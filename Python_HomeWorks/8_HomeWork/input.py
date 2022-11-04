import csv
from itertools import groupby
from os import path


# def head_line_input():  # дополняем заголовок и отправляем в csv
#     column = input("Input the new column name: ")
#     if not path.exists('head_line.csv'):
#         with open('head_line.csv', 'w') as h:
#             h.write(column)
#     else:
#         with open('head_line.csv', 'a') as h_l:
#             h_l.write(';' + column)
#
#
def user_input():  # Добавили данные пользователя согласно заголовка и отправили в scv
    with open('head_line.csv', 'r', newline='') as h_l:
        reader = csv.reader(h_l)
        for row in reader:
            head_line = row[0].split(';')
    # row1 = next(reader)  # gets the first line
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


def thesaurus_abv():  # Читает из файла, упорядочивает по алфавиту и делает словарем согласно заголовкам.
    with open('users_lines.csv', newline='') as u_l:
        reader = csv.reader(u_l)
        # list_list = []
        # for line in reader:
        #     list_list.append(*line)  # ['Пахомова;Алефтина;Сергеевна', 'Васин;Василий;Васильевич;женат']
        result = sorted(reader, key=lambda word: word[0][
            0])  # ['Васин;Василий;Васильевич;женат', 'Пахомова;Алефтина;Сергеевна']
        # print(*sorted(list_list, key=lambda word: word[0][0])) #  Васин;Василий;Васильевич;женат Пахомова;Алефтина;Сергеевна
        # return result   # [['Васин;Василий;Васильевич;женат'], ['Пахомова;Алефтина;Сергеевна']]
        #print(result)
        with open('head_line.csv', newline='') as h_l:
            reader_1 = csv.reader(h_l)
            users_data = {}
            for row in reader_1:
                for k in row:
                    head = list(map(str, k.strip().split(";")))
                #print(head)
                for v in result:
                    for j in v:
                        l_ist = list(map(str, j.strip().split(";")))  # ['Васин', 'Василий', 'Васильевич', 'женат']
                        #print(l_ist)
                        # l_ist = []
                        # l_ist.append(" ".join(v.strip().split(";")))  # Васин Василий Васильевич женат
                    users_data = dict(zip(head, l_ist))
                    print(users_data)  # {'Фамилия': 'Пахомова', 'Имя': 'Алефтина', 'Отчество': 'Сергеевна'


# user_input()
thesaurus_abv()


# user_dic = {}
# for key in sorted(reader_1):  # Из фамилии с индексом [1] берем 1-ю букву с индексом [0]
#     key = [' '.join(k[0].split(';') for k in reader_1)]
# print(key)
# for row in reader_2:
# #     print(' '.join(row[0].split(';')))
# print(user_dic)

# data_export()
# print(data)
# def data_export():
#     with open('head_line.csv', newline='') as h_l:
#         with open('users_lines.csv', newline='') as u_l:
#             with open('data_base.csv', 'w') as f:
#                 reader_1 = csv.reader(h_l)
#                 reader_2 = csv.reader(u_l)
#                 writer = csv.writer(f)
#                 for row in reader_1:
#                     writer.writerow(row)
#                 for row in reader_2:
#                     writer.writerow(row)
