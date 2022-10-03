
# 4.Реализуйте алгоритм перемешивания списка.

import random 

n = int(input("Введите количество элементов: ")) 
input_list = [i for i in range(n)]  # [0, 1, 2, 3, 4]
# print(input_list)
result_list = input_list[:]

for i in range(n): 
    index_random = random.randint(0, n - 1)
    result_list[i], result_list[index_random] = result_list[index_random], result_list[i] 
print("Перемешанный список",result_list) 

# !!! randint - захватывает и верхнюю и нижнюю границу!!! Берет 2 элемента (не 1!!!), оба целые!!!

#==============================
"""
import random 
a = [1, 2, 3, 4, 10, 11, 23, 56] 
random.shuffle(a, random.random) 
print(a)
"""

#=================================
"""
from random import randrange

num = int(input())
nums_list = list(range(num)) # список от 1 до num
len_list = len(nums_list) # переменная, чтобы каждый раз не считать

print(nums_list)

for i in range(len_list):
    n_1 = randrange(len_list) # записываем значение в диапазоне длины списка.
    n_2 = randrange(len_list) # randrange - принимает стартовое положение, последнее и шаг.
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1] # меняем местами 
                                                                    # 2 случайные переменные.

print(nums_list)
"""