
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". 

# input_str = input('Input the text: ')
# text_1 = 'абв'
# input_list = input_str.split()
# result_list = []
# for word in input_list:
#     if text_1 not in word:
#         result_list.append(word)
# print(' '.join(result_list))

#================================

# from pdb import line_prefix
# from random import sample

# def list_rand_words(count: int, alp: str = 'абв'):       # формирует строку.
#     words_list = []
#     for i in range(count):
#         letters = sample(alp, 3)            # sample не берет дубликаты
#         words_list.append(''.join(letters))
#     return ' '.join(words_list)

# Верхняя функция свернутая в строку.
# def list_rand_words(count: int, alp: str = 'абв'):
#     return '',join(''.join(sample(alp, 3)) for _ in range(count))

# def simple_sentence(words: str)-> str:
#     return ' '.join(words.replace("абв", "").split())

# def simple_sentence(words: str) -> str:
#     return ' '.join(words.replace('абв', '').split())


# all_list = list_rand_words(int(input('Number of words: ')))
# print(all_list)
# print(simple_sentence(all_list))

# можно решить через filter (not 'абв')

#============================

# list comprehension

def string_edit(my_str, symbols):
    return (' '.join([word for word in my_str.split() if symbols not in word]))


input_str = input('Enter the text:\n')
text_res = input('Enter the necessary symbols to remove:\n')
print(string_edit(input_str, text_res))