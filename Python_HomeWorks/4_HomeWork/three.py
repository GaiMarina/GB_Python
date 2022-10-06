
# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
#    список неповторяющихся элементов исходной последовательности.

import numpy

def non_repeating_set(res_set):
    tuple_set = []
    for i in res_set:
        if res_set.count(i) > 1:
            continue
        else: 
            tuple_set.append(i)
    return tuple_set

items = numpy.random.randint(10, size=10)
items_set = list(items[:10])
print(*items_set)

print(*non_repeating_set(items_set))

