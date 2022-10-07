
# Функция map()
# На вход принимает функцию, которую нужно применить к набору данных.
# Применяет указанную функцию к каждому элементу итерируемого объекта и возвращает
# итератор с новыми объектами.
# Нельзя пройтись дважды!!!

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x + 10, li)) # Получаем набор данных, где каждое число увеличено на 10.

# print(li)

#==================================

# data = list(map(int, input().split()))  # По умолчанию здесь используются пробелы.
#                                         # Получили список в функцию map, преобразовали лист из строк 
#                                         # в лист из чисел.
# print(data)

#==================================

# data = map(int, '1 2 3 45 234 6'.split())   # цифры в столбик.

# for e in data:
#     print(e * 10)                           # Домножили, проверили, что числа.

#==================================

# Результат работы map - это некий итератор. 
# По итератору можно пробежаться только один раз => чтобы одни и те же данные использовать 
# несколько раз, нужно их где-то принудительно сохранить.
# => list()

# data = list(map(int, '1 2 3'.split()))

# for e in data:
#     print(e)

# print('--')    
    
# for e in data:
#     print(e)

#==================================

# Переделываем пример с .select() на map()
# Работает так же.

def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = where(lambda x: not x % 2, res)           # Лябмда для каждого x будет возвращать % 2
res = list(map(lambda x: (x, x ** 2), res))
# В качестве функции - lambda, принимающая x и возвращающая кортеж; 
# в качестве списка - предыдущий результат.
print(res)

