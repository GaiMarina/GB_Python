# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0,
#    и выдаёт номер четверти плоскости, в которой находится эта точка 
#    (или на какой оси она находится).
#    Пример:
#    x=34; y=-30 -> 4
#    x=2; y=4-> 1
#    x=-34; y=-30 -> 3

a = float(input('Enter point X coordinate: '))
b = float(input('Enter point Y coordinate: '))

if a != 0 and b != 0:
    if a > 0 and b > 0:
        print('This point is in the 1 quarter.')
    if a < 0 and b > 0:
        print('This point is in the 2 quarter.')
    if a < 0 and b < 0:
        print('This point is in the 3 quarter.')
    if a > 0 and b < 0:
        print('This point is in the 4 quarter.')
else:
    print('This point is on the coordinate axis.')
