
# КОРТЕЖИ - неизменяемые "списки"
"""
a, b = 3, 4                     # множественное присваивание
 
a = (3, 41, 4, 5)                      # добавили скобки и получился кортеж!
                                # для кортежа переменной достаточно 1-й.
print(a)
                                # обращаемся по индексу к конкр-му эле-ту
print(a[0])
print(a[-1])

a[0] = 12                       # !!!для кортежей присвоить по индексу значение не работает!!!
"""
#===============================
"""
t = ()
print(type(t))          # tuple

t = (1,)
print(type(t))          # tuple

t = (1)
print(type(t))          # int

t = (28, 9, 1990)
print(type(t))          # tuple

colors = ['red', 'green', 'blue']
print(colors)           # ['red', 'green', 'blue']

t = tuple(colors)
print(t)                # ('red', 'green', 'blue')
"""
#====================================
"""
# Распечатываем в столбик элементы кортежа.

a = (3, 41, 4, 5)

for item in a:
    print(item)
""" 
#==================================

# В рамках одного кортежа можно миксовать разные типы данных.

#==================================

# Можно распаковать кортеж в отдельные переменные.

from re import T


t = tuple(['red', 'green', 'blue']) # двойное преобразование: создаем список и преобразовываем в
                                    # кортеж. Распаковываем кортеж в 3 независимые переменные.
red, green, blue = T

print('r:{} g:{} b:{}'.format(red, green, blue))     # r:red g:green b:blue
