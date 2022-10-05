
# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
#    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#    Пример:
#    [2, 3, 4, 5, 6] => [12, 15, 16];
#    [2, 3, 5, 6] => [12, 15]

# l_ist = [2, 3, 8, 2, 7]
# new_list = []

# for i in range((len(l_ist) + 1) // 2): # range работает только с целыми! => деление //
#     new_list.append(l_ist[i] * l_ist[-i - 1])
# print(new_list)

#==========================

# дойти до середины списка. Другой способ

# print(5 // 2 + 5 % 2)
# print(4 // 2 + 4 % 2)

#=========================

# Если хотим оставить серединку в нечетном списке как есть.

from random import sample

def list_rand_nums(count: int):
    if count < 0:
        print('Negative value of the number of numbers!')
        return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)
    
    for k in range(len_list // 2): # !!! range не работает с дробными!!! Деление - // !!!
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])
    # в if можно попасть только по истине: 
    if len_list % 2: # если не кратен 2-м. Истина - что-то отличное от False и 0
                     # если кратно 2-м, то это 0, в if не попадем.
        res_list.append(list_nums[len_list // 2]) # Индекс с 0...
    return res_list
# Есть разница: делить на 2 кол-во элементов и делить на 2 кол-во эл-в, 
# но брать результат как индекс, который с 0 т.е.добавляет 1)
all_list = list_rand_nums(int(input('Number of numbers: ')))
print(all_list)
print(prod_pairs(all_list))
