
# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# через список

print('Enter a real number:', end = ' ')
num_list = list(input())
sum_dig = 0

for i in range(len(num_list)):
    if num_list[i] == '.':
        continue
    sum_dig += int(num_list[i])
print(sum_dig)

#==============================

# математически

print('Enter a real number:', end = ' ')
num = input()
# print(type(num))        #str
count = 10 ** (len(num) - 2)
# print(type(count))      #int
# print(count)
num = int(float(num) * count)
# print(num)
res = 0
while num > 0:
    res += num % 10
    num //= 10
print(res)


