
# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". 

input_str = input('Input the text: ')
text_1 = 'абв'
input_list = input_str.split()
result_list = []
for word in input_list:
    if text_1 not in word:
        result_list.append(word)
print(' '.join(result_list))

