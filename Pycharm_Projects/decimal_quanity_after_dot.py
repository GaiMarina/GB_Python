
# 1. Функция ищет кол-во знаков после "."
"""
def count_after_dot(num_str):
    if "." in num_str:
         return len(num_str.split(".")[1].rstrip("0"))
    else:
         return 0
"""

# print(count_after_dot(d))

#print(Decimal(str(d)).as_tuple().exponent*(-1))

#===================

# 1.2 Функция ищет кол-во знаков после "."
"""
def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
print(get_count(d))
"""
#===================
"""
# 1.3 Функция ищет кол-во знаков после "."

def get_precision(d):
    if '.' not in d:
        return 0
    # Получение строки после точки и возвращение ее длины
    return len(d[d.index('.') + 1:])

print(get_precision(d))
"""

#d = float(input('Input the necessary number precision from 0.0000000001 to 0.1: '))
#num = float(input('Input the real number: '))
#num_res = pi * Decimal(d) / Decimal(d)
#print(num_res)

#============================

# Зная нужное количество знаков после запятой, выводим нужное число с помощью Decimal.
# Здесь нам нужно знать точное число знаков.

# number = Decimal(num)
# number = 3 * number
# print(number) 

#=======================
