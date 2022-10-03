
# 5. Задать список, состоящий из произвольных чисел. Количество задает пользователь.
#    Определить присутствует ли в заданном списке число, заданное пользователем.

from random import sample       # sample c отрицательными не работает, надо их отсеть проверкой.

def num_in_list(count, number):
    if count < 0:
        return 'Error'
    my_list = sample(range(1, count * 2), count)
    print(my_list)

    if number in my_list:
        return 'Yes'
    return 'No'

print(num_in_list(int(input('Input the quantity of numbers: ')), int(input('Input the number to find: '))))