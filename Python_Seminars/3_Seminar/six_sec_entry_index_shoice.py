
# 6. Задать список состоящий из произвольных слов, количество задает пользователь.
#    Написать программу, которая находит индекc второго вхождения строки в список, либо отвечает, 
#    что 2-го вхождения нет.

from random import choices # choice - одно значение, choices - несколько.

def random_set(n, word):
    new_list = []
    for i in range(n):
        a = choices(word, k = 3) # k = 3 - сколько выбрать из списка.
        new_list.append(''.join(a)) # '', чтобы не было пробелов.
    return new_list

def find_num(li_st, obj):
    if li_st.count(obj) > 1: 
        print('Yes')
        a = li_st.index(obj)
        print(li_st.index(obj, a + 1)) # .index() ищет индекс: 
                                       #a + 1, чтобы искал со следующего индекса.
    else:
        print('-1')
result = random_set(30, 'abc')
print(result)
find_num(result, 'bcc')

