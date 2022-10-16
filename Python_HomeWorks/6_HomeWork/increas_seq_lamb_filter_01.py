# 2. Дан список чисел. Создайте список, в который попадают числа, описывающие возрастающую
#    последовательность. Порядок элементов менять нельзя.
#    Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.


# input_list = [1, 5, 2, 3, 4, 6, 1, 7]
# result_list = [input_list[0]] 
# for i in input_list[1:]:
#     if i > result_list[-1]:
#         result_list.append(i)
# print(*result_list)

#===============================

# filter(), lambda

input_list = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = [input_list[0]] 
result_list += filter(lambda x: x > result_list[-1], input_list)
print(*result_list)