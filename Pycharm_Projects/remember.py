
# !!! Ввод списка целиком через пробел. 

# entered_list = input().split() 
"""
entered_list = input("Введите список чисел, разделенных пробелом: ").split() 

print("Введенный список:", entered_list) 
# Введенный список: ['1', ' 2', ' 3', ' 4', ' 5']
"""
#============================

# Повторный запрос на ввод заданное количество раз.

"""
for i in range(5): 
    i = int(input('Введите число: '))

num = i

if num > i: 
    i = num 

print(i) 
"""

#===========================

"""
# Замена символа конца строки.

a = int(input('Введите число N '))

for i in range(-a, a + 1):   
    print(i, end = ' ')
"""

#===========================
"""
# функция round

a = 1.312312
b = 3
c = (a * b)
d = round(a * b, 5) # количество знаков после запятой. 
                    # round округляет по мат.правилам!!!
print(c)
print(d)

# f

f"{8 / 7:.4f}" # '1.1429'

f"{8 / 7:.4}"  # '1.143' Без f - просто 4 цифры, а не после запятой.
"""
#=============================
"""
# Ввод/вывод данных

print('Введите a')
a = input()

print('Введите b')
b = input()

print(a, b)

print('{} {}'.format(a,b))

print(f'{a} {b}')
"""
#=============================
"""
text = 'съешь ещё этих мягких французских булок'
print(text[0:len(text):6])  # сеикакл           C нуля по всей длине с шагом 6.
print(text[::6])            # сеикакл           шаг - 6
"""
#=============================
"""
exit() # функция позволяет не выполнять код, записанный далее в скрипте.
"""
#=============================
"""
# копии

new_per = per - как два ярлыка

new_per = per[:] - не глубокая

# для вложенных списков, глубокая копия deep copy

import copy

new_per = copy.deepcopy(per)
"""
#============================
"""
# вложенный список с неглубокой копией

nested_list = [[1, 2], [3, 4]]
nested_list = nested_list[:]
nested_list[0].append(5)
print(nested_list)
"""
#============================
"""
# вложенный список с deepcopy

nested_list = [[1, 2], [3, 4]]

nested_list[0].append(5)
print(nested_list)
new_list = copy.deepcopy(nested_list)
new_list[0].append(5)
print(new_list)
"""
#============================

# отсекаем все, что после запятой

a = 0.987987
a = int(a)
print(a)

n = a % 1
print(n)