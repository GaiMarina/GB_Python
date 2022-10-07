
# List Comprehension нужен, чтобы быстро создавать списки.

# [exp for item in iterable]
# [exp for item in iterable (if conditional)] Выборка по условию
# [exp <if conditional> for item in iterable (if conditional)]

list = []

for i in range(1, 21):
    if(i % 2 == 0):
        list.append(i)
        
print(list)

list = [i for i in range(1, 21) if i % 2 == 0] # Кратко переписали верхний цикл.

print(*list)

#============================

# захотели создать пару каждого из чисел: кортежи.

list = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(*list)
# (2, 2) (4, 4) (6, 6) (8, 8) (10, 10) (12, 12) (14, 14) (16, 16) (18, 18) (20, 20)

#===========================

# Добавили возведение в 3-ю степень.

def f(x):
    return x ** 3

list = [f(i) for i in range(1, 21) if i % 2 == 0]
print(*list)
# 8 64 216 512 1000 1728 2744 4096 5832 8000

#==============================

# Еще раз добавляем кортеж. 

def f(x):
    return x ** 3

list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(*list)
