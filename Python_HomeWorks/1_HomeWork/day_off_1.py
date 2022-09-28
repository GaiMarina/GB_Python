# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#    и проверяет, является ли этот день выходным.
#    Пример:
#    6 -> да
#    7 -> да
#    1 -> нет

num = int(input('Input the number of the day: '))

while num < 1 or num > 7:
    num = int(input('Wrong input. Try again here: '))
if num == 6 or num == 7:
    print('Yes')
else:
    print('No')

#==============================
"""
num = int(input())

if 5 < num < 8:
    print('Weekend')
elif 0 < num < 6:
    print('Workday')
else:
    print("It's not the day of the week")
"""