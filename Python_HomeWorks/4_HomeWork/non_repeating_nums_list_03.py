
# 3. Задайте последовательность чисел. Напишите программу, которая выведет
#    список неповторяющихся элементов исходной последовательности.


# import numpy
# from collections import Counter


# items = numpy.random.randint(10, size=10)
# items_set = list(items[:10])
# print(*items_set)

# dict_new = Counter(items_set)
# res_list = [i for i in dict_new if dict_new[i] == 1]

# print(*res_list)


# =========================

# dict_new = {}

# items = numpy.random.randint(10, size=10)
# items_set = list(items[:10])
# print(*items_set)

# for i in items_set:
#     if not i in dict_new:
#         dict_new[i] = 0
#     dict_new[i] += 1

# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)
# print(*res_list)


# ===========================

# .count() Забирает много памяти.

# def non_repeating_set(res_set):
#     tuple_set = []
#     for i in res_set:
#         if res_set.count(i) > 1:
#             continue
#         else:
#             tuple_set.append(i)
#     return tuple_set


# items = numpy.random.randint(10, size=10)
# items_set = list(items[:10])
# print(*items_set)

# print(*non_repeating_set(items_set))

# ============================

# from collections import Counter
# from random import randint def create_list(k, m, n): # создание списка случайных чисел указанного диапазона в соответствии с указанным количеством элементов return [randint(m, n) for i in range(k)] k = int(input("Введите количество чисел в списке: ")) m = int(input("Введите нижнюю границу чисел: ")) n = int(input("Введите верхнюю границу чисел: ")) input_list = create_list(k, m, n) output_list = [k for k, v in Counter(input_list).items() if v == 1] print("Исходная последовательность чисел: ", input_list) print("Неповторяющиеся числа: ", output_list)

# ==============================

from random import randrange


def list_rand_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


def uniq_el(list_nums: list):
    result = []
    # 0 в значении ==> перебираем эле-ты списка ?
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:  # собираем ключи, которые имеют значение 1.
            result.append(k)

    return result


all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(uniq_el(all_list))

# Ключи в словаре д.б уникальными и не изменяемыми: число, строка, бул, кортеж, фикс.мно-во.
# .fromkeys() - можно подтянуть из к-то существ-го объекта как ключи, так и значения.
# Дубликаты словарь не делает, но сохранит существующий порядок.
