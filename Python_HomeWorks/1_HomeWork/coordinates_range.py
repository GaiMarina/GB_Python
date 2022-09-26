# 4. Напишите программу, которая по заданному номеру четверти, 
#    показывает диапазон возможных координат точек в этой четверти (x и y).
"""
quarter = int(input('Input the number of quater from 1 to 4: '))

while quarter < 1 or quarter > 4:
    quarter = int(input('Uncorrect input! Try again here: '))
if(quarter == 1):
    print("The possible quarter range equals x > 0, y > 0.")
if(quarter == 2):
    print("The possible quarter range equals x < 0, y > 0.")
if(quarter == 3):
    print("The possible quarter range equals x < 0, y < 0.")
if(quarter == 4):
    print("The possible quarter range equals x > 0, y < 0.")
"""
quarter = int(input('Input the number of quater from 1 to 4: '))

while quarter < 1 or quarter > 4:
    quarter = int(input('Uncorrect input! Try again here: '))
if(quarter == 1):
    print("The possible quarter range equals x > 0, y > 0.")
elif(quarter == 2):
    print("The possible quarter range equals x < 0, y > 0.")
elif(quarter == 3):
    print("The possible quarter range equals x < 0, y < 0.")
elif(quarter == 4):
    print("The possible quarter range equals x > 0, y < 0.")
