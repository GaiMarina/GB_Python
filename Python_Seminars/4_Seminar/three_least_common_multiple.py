
# 3. Задайте два числа. 
#    Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел. 

# Наименьшее общее кратное для нескольких чисел — это наименьшее натуральное число, 
# которое делится на каждое из этих чисел.

# def calculate_lcm(x, y): 
#     # selecting the greater number 
#     if x > y: 
#         greater = x 
#     else: 
#         greater = y 
#     while(True): 
#         if((greater % x == 0) and (greater % y == 0)): 
#             lcm = greater 
#             break 
#         greater += 1 
#     return lcm 
        
# # taking input from users
# num1 = int(input("Enter the first number: ")) 
# num2 = int(input("Enter the second number: ")) 
# # printing the result for the users 
# print("The L.C.M. of", num1,"and", num2,"is", calculate_lcm(num1, num2)) 
 
# ========================

# Задать два числа. Написать программу, которая находит НОК
# (наименьшее общее кратное) этих двух чисел.

import math

a = int(input())
b = int(input())

print(a * b // math.gcd(a, b))
