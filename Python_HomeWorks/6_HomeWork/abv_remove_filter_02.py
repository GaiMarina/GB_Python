# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# С текстом, задаваемом автоматически в случайном порядке.

from random import choices


# def random_set(n, word):
#     new_list = []
#     for a in range(n):
#         a = choices(word, k=6)
#         new_list.append(''.join(a))
#     return new_list


# def abv_removal(l_ist: list):
#     res_list = []
#     for word in l_ist:
#         if 'абв' not in word:
#             res_list.append(word)
#     return res_list


# random_line = random_set(20, 'абв')
# print(*random_line)
# print(*abv_removal(random_line))

# =============================

# filter(), lambda

def random_set(n, word):
    return ' '.join(str(b) for b in [''.join(choices(word, k=6)) for _ in range(n)])


def abv_removal(line: str):
    print(line)
    return ' '.join(filter(lambda x: 'абв' not in x, line.split(' ')))


print(abv_removal(random_set(20, 'абв')))
