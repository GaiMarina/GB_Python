
# МНОЖЕСТВА - содержат уникальные элементы. Элементы могут перемешиваться.
"""
colors = {'red', 'green', 'blue'}
print(type(colors))                     # <class 'set'>

colors.add('red')                       # .add()
print(colors)

colors.add('gray')
print(colors)

colors.remove('red')                    # .remove() - если точно удаляемый элемент там есть
print(colors)

colors.discard('red')                    # .discard() - вместо remove, не будет ошибки, 
                                         # если элемента нет.
print(colors)

# Сделать множество пустым.
colors.clear()
print(colors)
"""
#==========================
"""
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                    # .copy() Сделает копию мн-ва

u = a.union(b)                  # .union() объединит два мно-ва, но оставит уникальные эл-ты
# print(u)

i = a.intersection(b)           # .intersection() покажет общие элементы
# print(i)

dl = a.difference(b)            # .difference() покажет элементы в "a", которых нет в "b"
# print(dl)

dr = b.difference(a)            # .difference() покажет элементы в "b", которых нет в "a"
# print(dr)

q = a \
    .union(b) \
    .difference(a.intersection(b))
print(q)                        # {1, 21, 3, 13}
"""
#==========================

# неизменяемые множества

a = {1, 2, 3, 5, 8}
s = frozenset(a)                # frozenset
print(s)

#==========================