
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

positions = []
# with open(r'С:\nfile.txt', 'r', encoding='utf-8') as f:                   # r
# with open('С:\\nfile.txt', 'r', encoding='utf-8') as f:
with open('С:/Program Files/nfile.txt', 'r', encoding='utf-8') as f:        # самый подходящий
    positions = f.read().split()
    positions = [int(i) for i in positions]
n = int(input('Введите целое число: '))
s = []
for i in range(-n, n + 1):
    s.append(i)
result = 1
for i in range(len(positions)):
    result *= s[positions[i] - 1]
print(result)