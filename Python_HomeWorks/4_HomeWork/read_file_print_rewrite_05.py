
# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.

import enum
from importlib.resources import path


def read_file(file1):  # получение данных из файла
    with open(str(file1), 'r') as data:
        res_file = data.read()
    return res_file


f_ile = '/home/marina/Documents/GeekBrains/GB_Python/polynomial.txt'
file_1 = '/home/marina/Documents/GeekBrains/GB_Python/polynomial_1.txt'
temp_result = read_file(f_ile)
temp_2_result = read_file(file_1)

res_cut = ''
for i in temp_result:
    if i == '=':
        break
    res_cut += i

result = res_cut + '+ ' + temp_2_result

with open('pol_result.txt', 'a', encoding='utf-8') as the_file:
    the_file.write(result)

# ==========================

# 5. Даны два файла, в каждом из которых находится запись многочленов.
#    Задача - сформировать файл, содержащий сумму многочленов.

# from random import choice

# def poly_sum(name_1: str, name_2: str):
#     with open(name_1, 'r', encoding='utf-8') as my_f_1, \
#             open(name_2, 'r', encoding='utf-8') as my_f_2:
#         first = my_f_1.readlines() # .readlines() возвращает список строк всех, которые находятся в файле.
#         second = my_f_2.readlines()

#         if len(first) == len(second): # Условие совпадения количества строк.
#             with open('sum_poly.txt', 'a', encoding='utf-8') as my_f_3:
#                 for i, v in enumerate(first):           # enumerate - как range, но возвращает кортеж
#                         # состоящий из индекса и значения! Поэтому мы кортеж распаковывем в пер-х i и v!
#                     my_f_3.write(f'{v[:-5]} + {second[i]}') # отрезаем 5 от конца: = 0\n
#         else:
#             print('The contents of the files do not match!')


# # poly_sum(input('Enter the file name "text_1.txt": '), input('Enter the file name "text_2.txt": '))
# poly_sum('poly.txt', 'poly_2.txt')

# Вместо .readlines() др. способы в режиме чтения:
# .read() возвращает строки ==> можно .read().split() Можно .read().split('\n')
# .readline() прочитает только одну строку.
# Чтение физически перемещает курсор. Одно и то же чтение подряд, читает уже следующую (например, строку)

l_ist = ['d', 'e', 'w', 'q']

for i, v in enumerate(l_ist):
    print(i, v)

# ============================

# добавляем нумерацию:

l_ist = ['d', 'e', 'w', 'q']

for i, v in enumerate(l_ist, 100):
    print(i, v)

# ==============================

# Выводим красоту

l_ist = ['d', 'e', 'w', 'q']

for i, v in enumerate(l_ist, 1):
    print(f'{i}) {v}')  # i уберем, выведет только данные без номеров.
