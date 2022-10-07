
# enumerate()
# Функция enumerate() применяется к итерируемому объекту и 
# возвращает новый итератор с кортежами из индекса и элементов входных данных.
# Нельзя пойтись дважды.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

data = list(enumerate(users)) # <zip object at 0x7fa0ebd5e300> => нужен тип - list, например
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]
