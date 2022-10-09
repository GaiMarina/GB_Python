
# 5. Даны два файла, в каждом из которых находится запись многочлена. 
#    Задача - сформировать файл, содержащий сумму многочленов.

from importlib.resources import path

def read_file(file1): # получение данных из файла
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