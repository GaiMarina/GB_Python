
# Как из одного файла использовать функционал другого, в котором, например, хранятся функции.
# импортируем функцию из 1-й лекции.
"""
from cgitb import reset
from hashlib import new
import files_deal

print(files_deal.f(1))
"""
#===========================
"""
# Чтобы каждый раз не писать имя папки:

import files_deal as fld   # fld - альяс

print(fld.f(1))
"""
#===========================
"""
# Значения по умолчанию для функций.

def new_string(symbol, count):
    return symbol * count

print(new_string('!', 5))
print(new_string('!')) # TypeError missing 1 required...
"""
#===============================
"""
# Можно указать значение аргумента по умолчанию, чтобы не вводить потом.

def new_string(symbol, count = 3):
    return symbol * count

print(new_string('!', 5))   # !!!!
print(new_string('!'))      # !!!
print(new_string(4))        # 12

# !!! Python распознает тип данных в момент вызова функции!!!
# !!! Аргументов по умолчанию м.б. сколько угодно, но описываются они самыми последними!!!
"""
#===============================
"""
# Возможность передачи неограниченного количества аргументов.

# Ставим * перед названием набора аргументов...

def concatenatio(*params):
    res: str = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1'))           # a1
# print(concatenatio(1, 2, 3, 4,))      # TypeError: ...
"""
#=============================
"""
# Поменяли тип данных со строки на числа.

def concatenatio(*params):
    
    res: int = 0                        # тип данных поменяли
    
    for item in params:
        res += item
        
    return res

print(concatenatio(1, 2, 3, 4,))      # 10
"""
#=============================
"""
# Тип данных указывать не обязательно

def concatenatio(*params):
    
    res = 0                             # тип данных не указан
    
    for item in params:
        res += item
        
    return res

print(concatenatio(1, 2, 3, 4,))      # 10
"""
#=============================

# Рекурсия - ф-я вызывающая сама себя.ФИБОНАЧЧИ!

def fib(n):         # возвращение чисел фибоначчи. В 1-е - возвращаем 1, во 2-е, возвращаем 1!
    if n in [1, 2]:
        return 1
    else:           # иначе рекурсивный вызов для n-1 и n-2!
        return fib(n - 1) + fib(n - 2) 
    
list = []
for e in range(1, 10): # Можно посмотреть первые 10 чисел при необходимости.
    list.append(fib(e))
print(list)                 # 1 1 2 3 5 8 13 21 34

