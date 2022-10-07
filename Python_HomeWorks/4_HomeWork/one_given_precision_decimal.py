
# 1. Вычислить число c заданной точностью d
#    Пример:
#    при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Через метод .quantize() (позволяет вычислить число с заданной точностью).

from math import pi
from decimal import Decimal

# num = str(pi)                               # Можно использовать pi

# # num = input('Input the number: ')         # Можно использовать введенное число
# d = input('Input the necessary precision number d: ')

# # num = Decimal(num)
# # num = num.quantize(Decimal(str(d)))

# # num = Decimal(num).quantize(Decimal(d)) # 2 строки объединила.
# # print(num)

# print(Decimal(num).quantize(Decimal(d))) # еще 2 строки объединила.

#==============================

# Через функцию.

def num_precise(n_um, d_c):
    n_um = Decimal(n_um)
    n_um = n_um.quantize(Decimal(d_c))
    
    return n_um


num = input('Input the number: ')
d = input('Input the necessary precision number d: ')
print(num_precise(num, d))
