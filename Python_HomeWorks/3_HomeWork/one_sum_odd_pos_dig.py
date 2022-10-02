
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

# Без лишних слов.

li_st = input("Enter numbers separated by space: ").split()
s_um = 0

for i in li_st[1::2]:
    s_um += int(i)

print(f'The sum of numbers with the odd indices equals: {s_um}')




