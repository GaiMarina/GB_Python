
# # Встроенные типы и операции с ними.

# friend = 'Максим'
# #         012345

# # С 1 по 4-й

# print(friend[1:4]) # 1,2,3

# # С начала строки до 4-й

# print(friend[:4]) # 0,1,2,3

# # С 3 элемента до конца строки

# print(friend[3:]) # 3,4,5
#
# #Тип среза - класс str

# print(type(friend[1:4]))

# ===============================

# Методы

# friends = 'Марина Николай'

# # print(len(friends)) # C 1 - количество                          # len() - длина переменной
#
# print(friends.find('на')) # Индекс, на котором нашел.             .find('') - найти
# #                            # -1, если не нашел
# print(friends.split()) # Разбивает на строки через запятую, разделитель - пробел:
#                        # ['Марина', 'Николай']#                   .split('') - разбивка строки
# friends = 'Марина; Николай'
# print(friends.split(';'))
#
# print(friends.upper())                                            .upper()
# print(friends.lower())                                            .lower())
# ============================

# Способы склейки строк.

# name = 'Leo'
# age = 30

# # #1 конкатенация

# # hello_str = 'Привет, ' + name + ' тебе ' + str(age) + ' лет'
# # print((hello_str))
# #
# # #2 %

# hello_str = 'Привет %s тебе %d лет'%(name, age)
# print(hello_str)
#
# #3 format
# hello_str = 'Привет {} тебе {} лет'.format(name, age)
# print(hello_str)

# =================================

# Дана строка: "Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов
# Результат - поздравляем 1-ые 3 места: "Поздравляем 1.ИВАНОВ 2.ПЕТРОВ 3.СИДОРОВ с успехом!"
# top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
# start = top5.find('1')
# end = top5.find('4')
#
# top3 = top5[start: end]
#
# result = 'Поздравляем {} с успехом!'.format(top3.upper())
#
# print(result)
# ==============================================================

# СПИСКИ (LIST)

# Пустой список

# empty_list = []
#
# # заполненный элементами список

# friends = ['Max', 'Leo', 'Kate']
#
# # тип списка - list
# print(type(friends))
#
# # Доступны индексы (с 0)

# print(('Второй друг: ', friends[1]))
# print('Первый друг с конца', friends[-1])
#
# # Можно применить срезы

# print(friends[1:2])
# print(friends[:2])
# print(friends[1:])

# ===================================================
"""
friends = ['Max', 'Leo', 'Kate']

print (friends)

# len() - количество элементов
print(len(friends))

# .append() - добавить элемент
friends.append('Ron')
print (friends)
print(len(friends))

# .pop() - удалить последний элемент

print(friends.pop())
print(friends)
print(len(friends))

# .clear - очистить список

friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']

# .remove() - удаление элемента по значению

friends.remove('Kate')
print(friends)

# del - удаление по индексу.

del friends[0]
print(friends)
"""
#==========================

# оператор in
"""
hero = 'Superman'
# hero = 'Super'

if hero.find('man') != -1:
    print('Есть')
if 'man' in hero:
    print('Есть')

goals = ['стать гуру языка python', 'здоровье', 'накормить кота']
if 'здоровье' in goals:
    print('Все хорошо')
"""
#==========================
"""
# Программа winners, интерактивное награждение победителей соревнований по Python
# Пользователь вводит кол-во участников соревнований по python
# Пользователь вводит участников и их места в зависимости от кол-ва
# 1. Вывод имен участников по алфавиту
# 2. Получить 3-х победителей и поздравить их
# 3. Победители: ... Поздравляем!
print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место '.format(i))
    members.append(name)
    i -= 1

# Кто участвовал в соревновании по алфавиту (sorted())
print('В соревновании участвовали: ', sorted(members))

# мы записали людей с конца? .reverse, чтобы перевернуть список

members.reverse()
# нам нужно взять первые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)
"""
#=================================

# for для последовательностей (позволяет не применять цикл while)
# for позволяет перебирать элементы последовательности по порядку без указания индекса
# while
"""
friend_name = 'Max' # строка
friends = ['Max', 'Leo', 'Kate'] # список
roles = ('admin', 'guest', 'user') # кортеж

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1
# for in
for friend in friends:
    print(friend)

print('end')

for letter in friend_name:
    print(letter)

print('end')

for role in roles:
    print(role)

print('end')
"""
#================================

# функция range

# winners = ['Max', 'Leo', 'Kate']
"""
# простой перебор

for winner in winners:
    print(winner)

# Если нужно вывести место победителя?

# вывести нечетные цифры от 1 до 5

numbers = [1, 3, 5]

for number in numbers:
    print(number)
    
# А если цифр будет не 3, а 1000?

# Функция range позволяет вывести последовательность целых чисел. Чаще с for

numbers = range(10)
print(numbers)
print(type(numbers))

print(list(numbers)) # привели к типу list

numbers = range(66) # последняя цифра не входит
print(list(numbers))
"""
# for i in range(len(winners)):
#     #print(i)
#     print(i + 1,')', winners[i])

#=====================================

# вывести нечетные цифры от 1 до 5
numbers = [1, 3, 5]

# for number in numbers:
#     print(number)
# # выведет в линию
# print(list(range(1, 1000, 2))) # (начало (start), конец(stop), шаг(step))
# # выведет в столбик
# for number in range(1, 1000, 2):
#     print(number)

# for i in range(1, len(winners) + 1):
#     print(i,')', winners[i-1])

# =========================================

# СЛОВАРЬ
# friends = ['Max', 'Leo', 'Kate']
# print(friends)
# print(type(friends)) # <class 'list'>
# friend = friends[0]
# print(friend)
# print(type(friend)) # <class 'str'>
# какой будет тип, если добавить возраст?
# позже научимся свой тип создавать, а пока...словарь...
# friend = {
#     'name': 'Max',
#     'age': 23 # можно указывать все, что угодно: пол, имеет ли машину.
# }
# print(friend)
# print(type(friend))
#
# print(friend['age'])
#
# friend['has_car'] = True # Значение добавится!
# print(friend)
#
# friend['has_car'] = False # Значение поменяется, а не добавится!
# print(friend)

# удалим элемент
# del friend['age']
# print(friend)
# оператор if. Проверить есть ли такой-то ключ в словаре.
# if 'age' in friend:
#     print('Есть возраст')
#
# if 'has_car' in friend:
#     print('Есть машина')

#=====================================

# friend = {
#     'name': 'Max',
#     'age': 23,
#     'has_car': True
# }
# по ключам
# for key in friend.keys():
#     print(key) # печатаем ключи
#     print(friend[key]) # печатаем значения
#
# for key in friend: # работает точно так же
#     print(key) # печатаем ключи
#     print(friend[key]) # печатаем значения

# по значениям
# for val in friend.values():
#     print(val)

# пары: ключ/значение
# будем перебирать пары в форме кортежа
# for item in friend.items(): # .items возращает список из кортежей
#     print(item)
# чтобы получить в одну переменную ключ, а в другую значение:
# for key, val in friend.items():
#     print(key)
#     print(val)

#============================

# # МНОЖЕСТВА Не может быть 2-х одинаковых элементов.
# # Запись как словарь, но только со значениями.
# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
#
# print(type(cities)) #<class 'list'>
# print(cities)
#
# # Если хотим сделать список неповторяющихся элементов
# cities = set(cities)
#
# print(cities)
# print(type(cities)) #<class 'set'> множества. Дубли убрались.
#
# cities = {'Paris', 'Las Vegas', 'Moscow', 'Las Vegas'}
# print(cities)
# ===================================
# Действия с множествами
# объединение, пересечение, вычитание
# Семейная пара собирается в отпуск
# Каждый из супругов собирает в поездку вещи
# Max взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
# Какие вещи взяли супруги
print(max_things | kate_things)
# Какие вещи повторяются
print(max_things & kate_things)
# какие вещи взял Max, но не взяла Kate
print(max_things - kate_things)
# Какие вещи взяла Kate, но не взял Max
print(kate_things - max_things)


