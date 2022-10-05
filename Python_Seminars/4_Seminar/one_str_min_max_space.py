
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

# nums = [int(i) for i in input('Введите числа через пробел: ').split()] # list comprehension
# print(nums)
# print(max(nums), min(nums)) 
# print(max(nums), min(nums), sep= ' + ') 
# print(str(max(nums)) + ' ' + str(min(nums)))
# print(f'{max(nums)} {min(nums)}')

#==========================

# убираем отрицательность, проверяем на цифры.

def check(line):
    arr = line.split()
    for i in arr:
        if not i.strip('-').isdigit(): # Проверили цифры или нет. .strip() - убрали "-"
                                       # .strip() используется не только к 1 символу, даже к строке.
            return []
    return arr

# !!! Если функция возвращает несколько результатов, делаем кортеж!!!

def min_max(array):
    if array: # попадем в цикл, если массив не пустой.
        return min(array, key=int), max(array, key=int) 
    # key= - чтобы рассматривал значение списка, как целочисленный!
    return [] # Если попали в if, не попадем в else, поэтому можно убрать.
    
f = check('2 25 -36 87 7 -8 6')
print(min_max(f))
