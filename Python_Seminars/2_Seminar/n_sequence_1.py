
# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. 
#    (умножаем на -3) 
#    Пример: # Для N = 5: 1, -3, 9, -27, 81 
"""
n = int(input("Введите чило N: ")) 
j = 1 
list1 = [] 
for i in range(1, n + 1): 
    list1.append(j) 
    # print(j, end = ", ") # докрутить для последнего символа 
    j = j * -3 
print(list1) 
"""
#=========================

n = int(input("Введите чило N: ")) 
j = 1 
list1 = [] 
for i in range(1, n + 1): 
    list1.append(str(j))  # чтобы джойн с работал, в str
    # print(j, end = ", ") # докрутить для последнего символа 
    j *= -3 
print(", ".join(list1))                                         # .join()

