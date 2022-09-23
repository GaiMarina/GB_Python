
# name = input('Как тебя зовут: ')
# print('Привет', name)
#=======================================
# Если возраст меньше 18 лет, вывести на экран "Доступ запрещен"

# age = int(input('Введите свой возраст: '))
# if age < 18:
#     print('Доступ запрещен')
# elif age == 18:
#     print('Вам ровно 18 лет')
#     print('Что с вами делать?')
# # Иначе вывести на экран "Доступ разрешен"
# elif age > 18 and age < 25:
#     print('Отдельная категория пользователей')
# else:
#     print('Доступ разрешен')
# # Проверим на юбилей
#     if age % 5 == 0:
#         print('Поздравляем! У вас юбилей!')
#==============================================
# number = 43
# value = int(input('Введите число от 1 до 100'))
#
# if value == number:
#     print('Вы угадали!')
# else:
#     if value > number:
#         print('Нужно меньше')
#     else:
#         print('Нужно больше')
# =================================
# цикл while
# Задавать вопросы, пока пользователь не введет правильный ответ

# name = input('Кто создатель python? ')
#
# while name != 'Гвидо':
#     print('Не верно')
#     name = input('Кто создатель python? ')
#
# print('Верно')
# ====================================
# 1.вывод чисел от 0 до 100
# number = 0
#
# while number <= 100:
#     print(number)
#     # number = number + 1
#     number += 1
# ===============================
# 2.вывод чисел от 0 до n

# number = 0
# n = int(input('Введите n: '))
#
# while number <= n:
#     print(number)
#     # number = number + 1
#     number += 1
# =================================
# 3.вывод четных чисел от 0 до n
# number = 0
# n = int(input('Введите n: '))
#
# while number <= n:
#     if number % 2 == 0:
#         print(number)
#     # number = number + 1
#     number += 1
# =======================
# Использование  break

# name = None # Теперь вход в цикл - обязателен!
#
# # while name != 'Гвидо':
# while True:
#     name = input('Кто создатель python? ')
#     if name == 'Гвидо':
#         break
#     print('Не верно')
#
# print('Верно')
# ================================
# Использование continue. Вывод нечетных
# number = 0
# n = int(input('Введите n: '))
#
# while number <= n:
#     if number % 2 == 0:# Если четные - continue, если нечетные - print
#         number += 1
#         continue
#     print(number)
#     number += 1
# ===============================
# else после while
number = 0

while number <= 100:
    print(number)
    number += 1
    #if number == 33:
        #break
else:
    print('else - end')
print('end')
# ===========================
