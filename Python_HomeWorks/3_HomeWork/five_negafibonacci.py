
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#    Пример:
#    для k = 8 список будет выглядеть так: 
#    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
"""
k = int(input('Enter a number: '))

def fib(k):
    if k in [1, 2]:
        return 1
    else:
        return fib(k - 1) + fib(k - 2) 
    
list_1 = []
for e in range(1, k + 1):
    list_1.append(fib(e))
list_1.insert(0, 0)

list_2 = list_1[:]

for i in range(1, k + 1):
    if i % 2 != 0:
        list_1.insert(0, list_2[i])
        continue
    else:
        list_1.insert(0,list_2[i] * -1)
        
print(list_1)
"""
#=============================

a = (int(input('Введите число: ')))
l_ist = [0]

for i in range(1, a + 1):
    if i == 1:
        l_ist.append(1)
        l_ist.insert(0, 1)
    else:
        a = l_ist[-1] + l_ist[-2]
        l_ist.append(a)
        l_ist.insert(0, a * (-1) ** (i - 1))
print(l_ist)