
# 2. Напишите программу, которая принимает на вход число N и выдает набор 
#    произведений чисел от 1 до N.
#    *Пример:*
#    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter the number: '))
res_list = []
j = 1

for i in range(1, n + 1):
    res_list.append(j)
    i += 1
    j *= i 
print(f'List of the products of numbers from 1 to {n}:', res_list) 
