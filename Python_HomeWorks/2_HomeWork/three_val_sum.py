
# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#    *Пример:*
#    Для n = 6: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44, 5: 2.49, 6: 2.52}

n = int(input('Enter the number n: '))
dic = {}
su_m = 0

for i in range(1, n + 1):
    dic[i] = f'{(1 + 1 / i) ** i:.2f}'
    su_m += float(dic[i])
print(f'For n = {n}: {dic}')
print(f'The sum of values equals: {su_m}')

#=========================

# Решение с семинара
"""
n = int(input("Введите целое положительное число N: ")) 
res_list = [] 
sum1 = 0 

for i in range(1, n + 1): 
    res_list.append(round(((1 + 1/i) ** i), 2)) 
    sum1 += round(((1 + 1/i) ** i), 2) 
print(f"Для N = {n} последовательность чисел: \
    {res_list} \nСумма чисел последовательности равна {sum1}") 
"""