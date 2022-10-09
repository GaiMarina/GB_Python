
# 2. Задайте натуральное число N. Напишите программу, которая составит список 
#    простых множителей числа N.

import math


def prime_factors(n):
    l_ist = []
    while n % 2 == 0:
        l_ist.append(2)
        n = n / 2
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while(n % i == 0):
            l_ist.append(i)
            n = n / i
            
    if n > 1:
        l_ist.append(int(n))
    return l_ist
        
        
num = int(input('Enter the number N for calculation: '))
print(*prime_factors(num))
