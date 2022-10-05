
# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Пример:
#    45 -> 101101
#    3 -> 11
#    2 -> 10
"""
n = int(input('Enter a number: '))
res = ''

while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)
"""
#=========================

# n = int(input('Enter a number: '))
# print(bin(n)[2:])

#===========================

# Функцией с выводом в список.

def conv_bin(num: int):
    list_nums = []
    
    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2
    print(*list_nums, sep='') # * - распаковывает список без скобок через пробел.
                              # sep= - показывает, что разделителя быть не должно.
    
conv_bin(int(input("Input number: ")))

