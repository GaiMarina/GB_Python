
# как работают скопированные списки
"""
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1

for e in list_1:
    print(e)
    
print()                         # вывод пустой строки

for e in list_2:
    print(e)
    
print()
    
list_1[0] = 123
list_2[1] = 234                 # меняя значения 2-го списка, меняем значения исходного

for e in list_1:
    print(e)
    
print()

for e in list_2:
    print(e)                    # оба списка изменились
"""
#=========================
"""
# удаление последнего элемента списка

list_1 = [1, 2, 3, 4, 5]
print(list_1)

list_1.pop()
print(list_1)

list_1.pop()
print(list_1)

list_1.pop()
print(list_1)
"""
#=========================

# удаляем элемент по индексу через .pop()

list_1 = [1, 2, 3, 4, 5]
print(list_1)
# print(list_1.pop(2))            # выводит элемент, который удалил
# print(list_1)

# вставляем элемент по индексу через .insert()

# print(list_1.insert(2, 11))        # 2 - индекс, 11 вставляем на место с иднексом 2.
# print(list_1)

# просто добавить элемент в конец можно через .append()

print(list_1.append(11))
print(list_1)
