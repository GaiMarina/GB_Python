
# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# [(2, 4), (8, 64), (38, 1444)]

# path = '/home/marina/Documents/GeekBrains/GB_Python/Python_Lectures/3_Python_Lecture/file.txt'
# f = open(path, 'r')
# data = f.read() + ' '  # Считываем в строчке то, что есть и добавляем пробел.
# f.close()

# numbers = []

# while data != '':                           # Пробегаемся по всей строке и делаем проверку: пока
#     # моя строка не пустая.
#     space_pos = data.index(' ')             # Ищем первую позицию пробела.
#     # Взять все, что находится от первого символа до
#     numbers.append(int(data[:space_pos]))
#     # позиции первого пробела.
#     # Превращаем это в число и добавить в список номеров.
#     data = data[space_pos + 1:]
#     # Добавить в список чисел.
# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e ** 2))
# print(*out)

# ==========================

# Улучшаем код.


def select(f, col):               # Принимает функцию и набор данных.
    # Будем формировать новый список и сразу же его возвращать.
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
res = select(int, data)
# Лябмда для каждого x будет возвращать % 2
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
# В качестве функции - lambda, принимающая x и возвращающая кортеж;
# в качестве списка - предыдущий результат.
print(res)
