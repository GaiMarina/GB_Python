
# 1. В файле находится N натуральных чисел, записанных через пробел. 
#    Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
#    Найдите это число. 


def read_numbers(file): # получение данных из файла
    with open(str(file), 'r') as data:
        numbers = data.read()
    return [int(i) for i in numbers.split()]


file_1 = '/home/marina/Documents/GeekBrains/GB_Python/Python_Seminars/5_Seminar/numbers.txt'
temp_result = read_numbers(file_1)
for i in range(1, len(temp_result)):
    if temp_result[i - 1] != temp_result[i] - 1:
        print(temp_result[i - 1] + 1)

print(temp_result)

