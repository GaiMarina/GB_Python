
# 2. Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую
#    последовательность. Порядок элементов менять нельзя.
#    Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

from random import choices


input_list = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = [input_list[0]] 
for i in input_list[1:]:
    if i > result_list[-1]:
        result_list.append(i)
print(*result_list)

# =====================


# def new_list(size):
#     list_of_numbers = choices(range(1, size * 2), k=size)
#     return list_of_numbers


# n_list = new_list(10)
# print(n_list)


# def nums_range(new_list: list):
#     my_list = []
#     for i in range(len(new_list)):
#         f = new_list[i]
#         l_ist = [f]
#         for x in range(i + 1, len(new_list)):
#             if new_list[x] > f:
#                 f = new_list[x]
#                 l_ist.append(f)
#         if len(l_ist) > 1:
#             my_list.append(l_ist)
#     return my_list


# print(nums_range(n_list))

