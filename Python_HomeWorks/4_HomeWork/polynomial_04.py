
# 4. Задана натуральная степень k.
#    Сформировать случайным образом список коэффициентов
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import choice
from audioop import reverse
import random


def polynomial_to_file(degree):

    while degree < 0:
        degree = int(input('Error. Try again here: '))

    l_ist = [i for i in range(101)]
    plus_minus_list = ['+', '-']
    c_ount = [j for j in range(degree + 1)]
    c_ount.reverse()

    res_str = ''
    for i in c_ount:

        r_num = random.choice(l_ist)
        r_op = random.choice(plus_minus_list)

        if r_num != 0 and r_num != 1 and i != 1 and i != 0:
            res_str += r_op + ' ' + str(r_num) + '*x^' + str(i) + ' '
            continue
        elif r_num == 1 and i != 1 and i != 0:
            res_str += r_op + ' ' + 'x^' + str(i) + ' '
            continue
        elif r_num != 0 and r_num != 1 and i == 1:
            res_str += r_op + ' ' + str(r_num) + '*x' + ' '
            continue
        elif r_num != 0 and r_num != 1 and i == 0:
            res_str += r_op + ' ' + str(r_num) + ' '
        elif r_num == 0:
            continue
        elif r_num == 1 and i == 1:
            res_str += r_op + ' ' + 'x' + ' '
            continue
        elif r_num == 1 and i == 0:
            res_str += r_op + ' ' + 1 + ' '
            continue
        res_str += '= 0' + '\n'

    with open('polynomial_1.txt', 'w', encoding='utf-8') as the_file:
        the_file.write(res_str[2:])


polynomial_to_file(int(input('Enter the natural degree k: ')))


# Задана натуральная степень k. # Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. # Пример: # k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 # Pn(x)=аnхn+an-1xn-1+аn-2хn-2+....+а2х2+a1х+а0, from random import randint def create_list(k, m, n): # создание списка случайных чисел указанного диапазона в соответствии с указанной степенью уравнения return [randint(m, n) for i in range(k + 1)]
"""
def create_polynomial(input_list): # создание и форматирование многочлена на основании списка чисел polynomial_list = [] for i in range(len(input_list)): if input_list[-1 - i] != 0: polynomial_list.insert(0, str(input_list[-1 -i]) + "*x^" + str(i)) polynomial_str = " + ".join(polynomial_list) polynomial_str += " = 0" polynomial_str = polynomial_str.replace(" 1*", " ") polynomial_str = polynomial_str.replace("^1", "") polynomial_str = polynomial_str.replace("x^0", "1") polynomial_str = polynomial_str.replace("*1", "") if polynomial_str[0] == "1" and polynomial_str[1] == "*": n = 2 polynomial_str = polynomial_str[n:] return polynomial_str  
    
    k = int(input("Введите степень уравнения: ")) m = int(input("Введите нижнюю границу чисел: ")) n = int(input("Введите верхнюю границу чисел: ")) input_list = create_list(k, m, n) polynomial_list = create_polynomial(input_list) print(input_list) print(create_polynomial(input_list)) # with open('D:\\Обучение\\Практика\\Python\\Home_task4\\Polynomial_task004.txt', 'a') as data: # data.write(f"\n{create_polynomial(input_list)}") 
    
    def get_coeffs(digits): digits = digits.strip().strip(' = 0') digits = digits.split(' + ') coeffs = {} for i in digits: a, *b = i.split(' * x ** ') if b: coeffs[int(b[0])] = int(a) else: if i.endswith('x'): a, *b = i.split(' * x') coeffs[1] = int(a) else: coeffs[0] = int(i) return coeffs def sum_coeffs(d, coeffs): for key in d: if not key in coeffs: coeffs[key] = 0 coeffs[key] += d[key] return coeffs with open('res.txt') as f: digits1 = f.read() digits2 = digits1[:] coeffs1 = get_coeffs(digits1) coeffs2 = get_coeffs(digits2) coeffs = {} coeffs = sum_coeffs(coeffs1, coeffs) coeffs = sum_coeffs(coeffs2, coeffs) res = '' max_num = max(coeffs.keys()) for i, j in coeffs.items(): res += str(j) if i != 0 and j != 0 and i != 1: res += ' * x ** ' res += str(i) res += ' + ' elif j == 0: continue eli 
    
    elif i == 1: res += ' * x + ' else: res += ' = 0' print(res) 
"""
# ============================

# 4. Задана натуральная степень k.
#    Сформировать случайным образом список коэффициентов
#    (значения от 0 до 10) многочлена и записать в файл полученный многочлен не менее 3-х раз.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# def polynomial(num: int):
#     if num < 1:
#         return 0

#     poly = ''
#     num_list = range(0, 10)

#     with open('poly.txt', 'a', encoding='utf-8') as my_f:
#         for i in range(num, 0, -1):     # вот как пойти по числу в обратном порядке)
#             # choice берет повторяющиеся, не уникальные эл-ты!!!
#             value = choice(num_list)
#             if value:                   # если зашел 0, внутрь не попадем.
#                 poly += f"{value}*x^{i} {choice('+-')}"
#                 # Менеджер контекста закрывает файлы автоматически!!!
#         my_f.write(f'{poly}{choice(num_list)} = 0\n')


# # _ в качестве безымянной переменной. Она особо значения не имеет.
# for _ in range(3):
#     polynomial(int(input('Enter ')))

# ============================

# Оптимизированный вариант.

# def polynomial_to_file(degree):

#     while degree < 0:
#         degree = int(input('Error. Try again here: '))

#     res_str = ''
#     nums_list = range(0, 100)
#     for i in range(degree, -1, -1):

#         r_num = choice(nums_list)
#         r_op = choice('+-')

#         if r_num:
#             if res_str:
#                 res_str += ' '
#             res_str += r_op + ' '
#             if i:
#                 if r_num != 1:
#                     res_str += str(r_num) + '*'
#                 res_str += 'x'
#                 if i != 1:
#                     res_str += '^' + str(i)
#             else:
#                 res_str += str(r_num)
#     res_str += ' = 0' + '\n'

#     with open('polynomial_1.txt', 'a', encoding='utf-8') as the_file:
#         the_file.write(res_str[2:])


# polynomial_to_file(int(input('Enter the natural degree k: ')))
