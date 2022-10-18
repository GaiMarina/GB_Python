

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

from importlib.resources import path
from itertools import groupby
from itertools import starmap
from mimetypes import init
from operator import index
from itertools import combinations
from platform import java_ver


# def read_data(path):
#     with open(path, 'r', encoding='utf-8') as data_file:
#         init_data = data_file.read()
#     return init_data


# def pack(path):

#     temp_result = read_data(path)
#     pack_data = ''

#     for i, j in groupby(temp_result):
#         pack_data += str(len(list(j))) + str(i)
#     print(pack_data)

#     with open('compression_RLE.txt', 'w', encoding='utf-8') as the_file:
#         the_file.write(pack_data)

#     print('\n' + '-' * len(pack_data))


# def composition(cnt, s):
#     return int(cnt) * s


# def decoding(init_s):
#     set_list = []
#     a, b = '', ''
#     for i in init_s:
#         if i.isalpha():
#             b = i
#             set_list.append((a, b))
#             a, b = '', ''
#         else:
#             a += i

#     print(set_list)
#     return set_list


# def unpack(path):

#     temp_2_result = read_data(path)
#     unpack_data = ''

#     unpack_data = ''.join(starmap(composition, decoding(temp_2_result)))
#     print(unpack_data)

#     with open('uncompression_RLE.txt', 'w', encoding='utf-8') as the_file:
#         the_file.write(unpack_data)

#     print('\n' + '-' * len(unpack_data))


# pack('/home/marina/Documents/GeekBrains/GB_Python/Python_HomeWorks/5_HomeWork/data.txt')
# unpack('/home/marina/Documents/GeekBrains/GB_Python/compression_RLE.txt')

# =====================================

# zip(), lambda

def read_data(path):
    with open(path, 'r', encoding='utf-8') as data_file:
        init_data = data_file.read()
    return init_data


def pack(path):

    temp_result = read_data(path)
    pack_data = ''

    # for i, j in groupby(temp_result):
    #     pack_data += str(len(list(j))) + str(i)
    # print(pack_data)
    pack_data += ''.join((str(len(list(j))) + str(i))
                         for i, j in groupby(temp_result))

    with open('compression_RLE.txt', 'w', encoding='utf-8') as the_file:
        the_file.write(pack_data)


# def composition(cnt, s):
#     return int(cnt) * s


def decoding(init_s):
    # set_list = []
    # a, b = '', ''
    # for i in init_s:
    #     if i.isalpha():
    #         b = i
    #         set_list.append((a, b))
    #         a, b = '', ''
    #     else:
    #         a += i

    numbers = ''.join(x if not x.isalpha() else " " for x in init_s).split()
    abv = list(''.join(x for x in init_s if x.isalpha()))
    set_list = list(zip(numbers, abv))

    return set_list


def unpack(path):

    temp_2_result = read_data(path)
    unpack_data = ''

    unpack_data = ''.join(starmap(lambda a, b: int(a) * b, decoding(temp_2_result)))

    with open('uncompression_RLE.txt', 'w', encoding='utf-8') as the_file:
        the_file.write(unpack_data)


pack('/home/marina/Documents/GeekBrains/GB_Python/Python_HomeWorks/5_HomeWork/data.txt')
unpack('/home/marina/Documents/GeekBrains/GB_Python/compression_RLE.txt')
