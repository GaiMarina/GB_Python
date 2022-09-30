
# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# через список
"""
num_list = list(input('Enter a real number: '))
sum_dig = 0

for i in range(len(num_list)):
    if num_list[i] == '.':
        continue
    sum_dig += int(num_list[i])
print(sum_dig)
"""
#==============================

# математически

num = input('Enter a real number: ')

counter = 10 ** (len(num))
num = int(float(num) * counter)

res = 0
while num > 0:
    res += num % 10
    num //= 10
print(res)


