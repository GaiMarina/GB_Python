

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


from random import choices


def random_set(n, word):
    new_list = []
    for a in range(n):
        a = choices(word, k=6)
        new_list.append(''.join(a))
    return new_list


def abv_removal(l_ist: list):
    res_list = []
    for word in l_ist:
        if 'абв' not in word:
            res_list.append(word)
    return res_list


random_line = random_set(20, 'абв')
print(*random_line)
print(*abv_removal(random_line))
