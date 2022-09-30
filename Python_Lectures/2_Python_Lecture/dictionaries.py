
# СЛОВАРИ - неупорядоченные коллекции произвольных объектов с доступом по ключу.
"""
dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# обратный \ нужен, чтобы не лепить все в одну строку
# print(dictionary)       # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary['left'])
"""
#============================
"""
# смотрим ключи

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }

for k in dictionary.keys():
    print(k)
"""
#============================
"""
# смотрим значения

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
for k in dictionary.values():
    print(k)
"""
#=============================

# Пробегаемся по всем элементам словаря

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
for v in dictionary:
    print(v)

for v in dictionary:
    print(dictionary[v])

# распечатаем по ключу
print(dictionary['up']) # ↑

# присвоем ключу другое значение
dictionary['up'] = 'up'
print(dictionary['up'])

