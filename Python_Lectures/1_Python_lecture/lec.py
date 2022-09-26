# можно выделить и запустить выполнение выделенного!
# типы данных и переменная
# int, float, boolean, str, list, None
"""
value = None # Можно объявить переменную без указания значения.

a = 123
b = 1.23

# print(type(a))
# print(type(b))

value = 12334
print(value)

# указать строку. \n - переход на новую строку

s = 'hello \nworld' 
print(s)

# escape последовательности

# Если дублируется апостров, писать внутренний после \

#==============================

a = 123
b = 1.23
s = 'hello world' 

# вывод нескольких строк

print(a, b, s)

print(a, '-', b, '-', s) 

# .format

print('{} - {} - {}'.format(a, b, s)) 

# Интерполяция
print(f'{a} - {b} - {s}') # переменные в скобках и вначале f. 

# указание, где какая переменная по индексу
print('{1} - {2} - {0}'.format(a,b,s))
#       b     s     a

#===========================

# логическая переменная

f = True

print(f)

#============================

# Вместо массивов - списки.

list = [1, 2, 3]
list = ['1', '2', '3', 'hello', ] # можно указывать переменные разных типов, но лучше исп-ть 1 тип.
print(list)

# Лишний пробел может убить программу...

#===============================

# Ввод/вывод данных

print('Введите a');
a = input()

print('Введите b');
b = input()

print(a, b)

print('{} {}'.format(a,b))

print(f'{a} {b}')

#=====================

# приведение к одному типу данных

print('Введите a ');
a = float(input())

print('Введите b ');
b = float(input())

print(a, ' + ' , b, ' = ', a+b)

#============================

# функция round

a = 1.312312
b = 3
c = (a * b)
d = round(a * b, 5) # количество знаков после запятой. 
                    # round округляет по мат.правилам!!!
print(c)
print(d)

#=======================

# Сокращенные операции присваивания

a = 3
a += 5

print(a)

#============================

# Логические операции

a = 1 > 4
print(a) # выведет False

a = 1 < 4 and 5 > 2
print(a) # True

a = 1 != 2
print(a)

# сравнить строки

a = 'qwe'
b = 'qwe'
print(a == b) # будет True

# сравнить списки

a = [1, 2]
b = [1, 2]
print(a == b)

# сравнить неравенства
a = 1 < 3 < 5 < 10
print(a)

func = 1
T = 4
x = 123

print(func < T > x ) # False

#===========================

# логические операции

f = 1 > 2 or 4 < 6
print(f)

"""

f = [1, 2, 3, 4]
print(f)
print(not 2 in f) # с not - отрицание. Можно без него.

is_odd = f[0] % 2 == 0 # проверка по индексу на четность.
print(is_odd)

# 0 - ложь
# 1 - истина
is_odd = not f[0] % 2 # отрицание 0 - 1
print(is_odd)