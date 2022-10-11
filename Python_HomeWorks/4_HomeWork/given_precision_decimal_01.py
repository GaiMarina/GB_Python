
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
# # num = num.quantize(Decimal(d))

# # num = Decimal(num).quantize(Decimal(d)) # 2 строки объединила.
# # print(num)

# print(Decimal(num).quantize(Decimal(d))) # еще 2 строки объединила.

# ==============================

# Через функцию.

# def num_precise(n_um, d_c):
#     n_um = Decimal(n_um)
#     n_um = n_um.quantize(Decimal(d_c))

#     return n_um


# num = input('Input the number: ')
# d = input('Input the necessary precision number d: ')
# print(num_precise(num, d))

# =====================


# def accuracy(num, acc):
#     number = Decimal(f'{num}') # Преобразование в строку через формат.
#     return number.quantize(Decimal(f'{acc}'))


# print(accuracy(float(input('Enter a real number: ')), float(input('Enter the required accuracy 0.0001: '))))

# =====================

num = float(input('Enter a real number: '))  # float => число уже .0

_, accu = input("Enter the required accuracy '0.0001': ").split(".")  # разделяет на целую часть и 0001
# нам нужна длина после 0001...
# Способ добавлять нули при форматировании. num: - означает, что начинается форматирование
print(f"{num:.{len(accu)}f}")
# Добавляем после точки длину дробной части.
