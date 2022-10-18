
# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.


# from importlib.resources import path


# def read_file(file1):  # получение данных из файла
#     with open(str(file1), 'r') as data:
#         res_file = data.read()
#     return res_file


# f_ile = '/home/marina/Documents/GeekBrains/GB_Python/polynomial.txt'
# file_1 = '/home/marina/Documents/GeekBrains/GB_Python/polynomial_1.txt'
# temp_result = read_file(f_ile)
# temp_2_result = read_file(file_1)

# res_cut = ''
# for i in temp_result:
#     if i == '=':
#         break
#     res_cut += i

# result = res_cut + '+ ' + temp_2_result

# with open('pol_result.txt', 'a', encoding='utf-8') as the_file:
#     the_file.write(result)

# =========================

# 5. enumerate()


from importlib.resources import path


def read_file(file):  # получение данных из файла
    with open(file, 'r') as data:
        res_file = data.readlines()
    return res_file


f_ile = '/home/marina/Documents/GeekBrains/GB_Python/Python_HomeWorks/6_HomeWork/file.txt'
file_1 = '/home/marina/Documents/GeekBrains/GB_Python/Python_HomeWorks/6_HomeWork/file_1.txt'
temp_result = read_file(f_ile)
temp_2_result = read_file(file_1)

if len(temp_result) == len(temp_2_result):
    for i, v in enumerate(temp_result):
        with open('pol_result.txt', 'w', encoding='utf-8') as the_file:
            the_file.write(f'{v[:-5]} + {temp_2_result[i]}')
else:
    print('The contents of the files do not match!')
