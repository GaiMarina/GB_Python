"""
# Нахождение максимума из 2-х чисел.

a = int(input('a = '))
b = int(input('b = '))

if a > b:
    print(a)
else: print(b)

#====================
# if - elif - else

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

#=============================

# while
# Переворачиваем число

original = 287
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

#=====================
# while else

original = 456
inverted = 0

while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
#    print(original)
else:
    print('Пожалуй')
    print('хватит )')

print(inverted)

#============================
# for
for i in 1, 2, 3, 4, 5:
    print(i ** 2)

list = [1, 2, 3, 4, 10, 5]
for i in list:
    print(i)

#============================
r = range(10) # Цифры с 0 до 10. 10 - не войдет.
for i in r:
    print(i)

# Можно без указания отдельной переменной
for i in range(10):
    print(i)

# Можно задать диапазон:
for i in range(1, 5):
    print(i)

# Можно получить разбивку строки: учтет и пробелы и знаки.
for i in 'Mari - na':
    print(i)

#==========================

# Строки

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ'))
"""
#=======================
"""
# Получить пояснение по функции

text = 'съешь ещё этих мягких французских булок'
#help(text.istitle)
help(int)


text = 'съешь ещё этих мягких французских булок'

print(text[0])              # c
print(text[1])              # ъ
print(text[len(text)-1])    # к
print(text[-5])             # б
print(text[:])              # print(text)
print(text[:2])             # съ
print(text[len(text)-2:])   # ок
print(text[2:9])            # ешь ещё
print(text[6:-18])          # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])            # сеикакл
text = text[2:9] + text[-5] + text[:2] # ..
"""
#=================================
"""
# Списки

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
ran = range(1, 6)
print(type(ran))

numbers = list(ran) # приведение к типу лист
print(type(numbers))

print(numbers)
numbers[0] = 10
print(f'{len(numbers)} len') # [10, 2, 3, 4, 5]
print(numbers)

numbers = [10, 2, 3, 4, 5]

for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]
"""
#=========================
"""
colours = ['red', 'green', 'blue']

for e in colours:
    print(e) # red green blue

for e in colours:
    print(e * 2) # redred greengreen blueblue

# .append - добавить в конец
colours.append('gray')
print(colours == ['red', 'green', 'blue', 'gray']) # True

# Удалить элемент. .remove() del colours[0]
colours.remove('red')
print(colours)
del colours[0]
print(colours)
"""
#==========================
# Функции. Можно миксовать разные типы данных.
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2
print(f(arg))
print(type(f(arg)))