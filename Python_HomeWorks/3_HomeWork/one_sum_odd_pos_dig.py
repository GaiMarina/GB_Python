
# 1. Задайте список из нескольких чисел. 
#    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#    Пример:
#    [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
li_st = input("Enter numbers separated by space: ").split()
print(f'The entered list is: {li_st}')

temp = []
s_um = 0

for i in li_st[1::2]:
    temp.append(str(i))
    s_um += int(i)
print('Numbers on the odd positions:', end = ' ')
print(", ".join(temp))
print(f'The sum of numbers with the odd indices equals: {s_um}')
"""
#============================
"""
# Без лишних слов.

li_st = input("Enter numbers separated by space: ").split()
s_um = 0

for i in li_st[1::2]: # С большим списком может перегрузить оперативку. Срез враз 
                      # вбирает в память все нечетные по условию.
    s_um += int(i)

print(f'The sum of numbers with the odd indices equals: {s_um}')
"""
#=====================

# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, которая найдет сумму элементов списка, стоящих 
# на нечетных позициях(не индексах)

from random import sample

def list_rand_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return[]
    
    list_nums = sample(range(1, count * 2), count) # range от 1 до двойного размера count, 
                                                   # в количестве count
    return list_nums

def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for k in range(0, len(list_nums), 2):
        sum_nums += list_nums[k]
    return sum_nums

all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(sum_odd_pos(all_list))