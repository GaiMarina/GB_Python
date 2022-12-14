
# Анонимные, lambda функции.

# def f(x):           # <class 'function'>
#     x ** 2

# g = f
# print(f(1))         # обе строки с f и g работают одинаково.
# print(g(1))

# # Можем в функцию в качестве аргумента передать другую функцию.

# def f(x):           # Подобная функция может пригодиться только раз за всю работу приложения
#                     # Как сократить.
#     return x ** 2

# print(f(2))

# # Сокращаем: Смотрим тип данных функции: функция ==> в функцию можно положить аргумент, др.фун-ю.

# def f(x):
#     return x ** 2
# g = f               # Сохраняем всю функцию целиком => g может быть использована как и f
#                     # У нас есть переменная g, которая хранит ссылку на функцию f.
# print(type(f))
# print(type(g))

# print(f(4))
# print(g(4))

# =========================

# def calc(x):
#     return x + 10

# print(calc(10))


# def calc2(x):
#     return x * 10

# print(calc2(10))


# def math(op, x):         # в качестве аргумента - операция (функция) и число.
#     print(op(x))


# math(calc2, 10)
# math(calc, 10)

# ============================

# Пример функции с двумя переменными.

# def sum(x, y):
#     return x + y

def sum(x, y): return x + y          # Это то же самое, что 2 строки выше.


def mult(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))
#    return op(a, b)


# calc(sum, 4, 5)
calc(lambda x, y: x + y, 4, 5)
