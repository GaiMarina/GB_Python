# 5. Напишите программу, которая принимает на вход координаты двух точек и 
#    находит расстояние между ними в 2D пространстве. 
#    Пример:
#    A (3,6); B (2,1) -> 5,09
#    A (7,-5); B (1,-1) -> 7,21
"""
from math import sqrt

ax = float(input('Enter the x coordinate of the point A: '))
ay = float(input('Enter the y coordinate of the point A: '))

bx = float(input('Enter the x coordinate of the point B: '))
by = float(input('Enter the y coordinate of the point B: '))

distance_2d = round(sqrt((bx - ax) ** 2 + (by - ay) ** 2), 2)
print(distance_2d)
"""
#==========================

ax = float(input('Enter the x coordinate of the point A: '))
ay = float(input('Enter the y coordinate of the point A: '))

bx = float(input('Enter the x coordinate of the point B: '))
by = float(input('Enter the y coordinate of the point B: '))

distance_2d = round(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5, 2)
print(distance_2d)

