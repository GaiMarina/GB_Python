
# 1. Задать строку из набора чисел. 
#    Написать программу, которая покажет большее и меньшее число.
#    В качестве символа_разделителя использовать пробел.

# map() — это встроенная функция, которая применяет функцию ко всем входным элементам итератора.

#nums = list(map(int, input('Введите числа через пробел: ').split()))

#nums = input('Введите числа через пробел: ').split()
#l_ist = [int(nums[i]) for i in range(len(nums))]
#l_ist = [int(i) for i in nums]
#print(l_ist)

# alt - shift - f

nums = [int(i) for i in input('Введите числа через пробел: ').split()] # list comprehension
print(nums)
print(max(nums), min(nums)) 
print(max(nums), min(nums), sep= ' + ') 
print(str(max(nums)) + ' ' + str(min(nums)))
print(f'{max(nums)} {min(nums)}')
