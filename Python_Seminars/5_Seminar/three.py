
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". 

input_str = input()
text_1 = 'абв'
input_list = input_str.split()
result_list = []
for word in input_list:
    if text_1 not in word:
        result_list.append(word)
print(' '.join(result_list))

# 1. В файле находится N натуральных чисел, записанных через пробел. # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число. def read_numbers(file): # Получение данных из файла with open(str(file), 'r') as data: numbers = data.read() return [int(i) for i in numbers.split()] file1 = "D:/Обучение/Практика/Python/Seminar5/numbers.txt" temp_result = read_numbers(file1) for i in range(1, len(temp_result)): if temp_result[i - 1] != temp_result[i] - 1: print(temp_result[i -1] + 1) print(temp_result) 

# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя. # Пример: # [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. input_list = [1, 5, 2, 3, 4, 6, 1, 7] result_list = [input_list[0]] for i in input_list[1:]: if i > result_list[-1]: result_list.append(i) print(result_list) 

#3. Напишите программу, удаляющую из текста все слова, содержащие "абв". input_str = input() text1 = "абв" input_list = input_str.split() result_list = [] for word in input_list: if text1 not in word: result_list.append(word) print(" ".join(result_list)) 