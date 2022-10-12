
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

from importlib.resources import path
from itertools import groupby
from itertools import starmap


def read_data(path):
    with open(path, 'r', encoding='utf-8') as data_file:
        compr_data = data_file.read()
    return compr_data


path = '/home/marina/Documents/GeekBrains/GB_Python/Python_HomeWorks/5_HomeWork/data.txt'
temp_result = read_data(path)

for i, j in groupby(temp_result):
    set_cut = [len(list(j)), i]
    set_str = "".join(map(str, set_cut))
    print(set_str, end='')
    with open('compression_RLE.txt', 'a', encoding='utf-8') as the_file:
        the_file.write(set_str)
