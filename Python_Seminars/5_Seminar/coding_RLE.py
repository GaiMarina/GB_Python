
from itertools import groupby, starmap
from os import path


def rle_encode(text='text.words.txt', code_text='text_code_words.txt'):
    if path.exists(text) and not path.exists(code_text):
        # Если существует, можем открыть, если не существует, можем создать.
        with open(text) as my_f_1,\
                open(code_text, 'w') as my_f_2:
            for i in my_f_1:  # вместо read, readline, readlines берет построчно, как итератор.
                my_f_2.write(''.join([f'{len(list(v))}{ch}'
                             for ch, v in groupby(i)]))
    else:
        print('The files do not exist in the system!')


# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:  # по умолчанию чтение 'r'
#             n = ''
#             for k in my_f:
#                 word_nums = []
#                 for i in k.strip(): # убираем в конце enter
#                     if i.isdigit():
#                         n += i
#                     else:
#                         word_nums.append([int(n), i]) # аппендит подсписок
#                         n = '' # n зачищается для перехода на новую букву.
#                 print(''.join(starmap(lambda x, y: x * y, word_nums)))
#     else:                                 # .stramap() перемножит lambda в список и вернет список.
#         print('The files do not exist in the system!')
                                            # word_nums содержит подсписки => x, y как раз цифра и буква.
def rle_decode(name):                       # .join() с пустыми кавычками => склеивает в одно длинное слово.
    if path.exists(name): # проверка на существование файла в системе.
        with open(name) as my_f:
            for i in my_f:
                word_nums = [''.join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
                # если какой-то элемент нашей строки .isdigit, то по нему и группирует.
                print(''.join([f'{int(word_nums[i]) * word_nums[i + 1]}' for i in range(0, len(word_nums), 2)]))
    else:               # перемножаем вручную, без starmap
        print('The files do not exist in the system!')


# Проверка на существование файлов в системе.
rle_encode(input('Enter the name of the file with the text: '),
           input('Enter the file name to record: '))

rle_decode(input('Enter the name of the file to decode: '))

# groupby - делает пару по похожести, кодирует, пока похоже: буква, количество.
