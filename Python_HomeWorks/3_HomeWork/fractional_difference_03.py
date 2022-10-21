
# 3. Задайте список из вещественных чисел. 
#    Напишите программу, которая найдёт разницу между максимальным и 
#    минимальным значением дробной части элементов.
#    Пример:
#    [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# num_list = [1.1, 1.2, 3.1, 5.1, 10.01]
# new_list = []

# for i in num_list:
#     j = round(i % 1, 2)
#     new_list.append(j)
# print(new_list)
# print(max(new_list) - min(new_list))

# =========================

# Задать список из произвольных вещественных чисел, количество которых задает пользователь.
# Написать программу, которая найдет разницу между максимальным и минимальным значением 
# дробной части элементов.

# from random import uniform

# def list_rand_nums(count: int):
#     list_nums = []
#     if count <= 0:
#         print('Negative value of the number of numbers!')
#         return[0.0]
    
#     for i in range(count):
#         list_nums.append(round(uniform(1, count), 2))
#     return list_nums

# def dif_max_min(list_nums: list):
#     num_max = num_min = list_nums[0] % 1
    
#     for k in range(1, len(list_nums)):
#         num = round(list_nums[k] % 1, 2)
#         if num > num_max:
#             num_max = num
#         elif num < num_min:
#             num_min = num
#     result = round(num_max - num_min, 2)
#     print(f'Min: {num_min}, Max: {num_max}. Difference: {result}')
#     return result

# all_list = list_rand_nums(int(input('Number of numbers: ')))  
# print(all_list)
# print(dif_max_min(all_list))

#====================================

# input_list = list(map(float, input('Enter the numbers separated by space: \n').split()))
input_list = list(map(lambda x: float(x), input('Enter the numbers separated by space: \n').split()))
fract_list = [round(i % 1, 2) for i in input_list if i % 1 != 0]
print(f'Fractional difference equals: {max(fract_list) - min(fract_list)}')
    