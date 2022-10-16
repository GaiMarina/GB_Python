# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +, -, /, * приоритет операций стандартный.
# * Добавьте скобки, приоритет операций меняется.
# Все элементы через пробел.


actions = {
    '^': lambda x, y: str(float(x) ** float(y)),
    '*': lambda x, y: str(float(x) * float(y)),
    '/': lambda x, y: str(float(x) / float(y)),
    '+': lambda x, y: str(float(x) + float(y)),
    '-': lambda x, y: str(float(x) - float(y))
}


res = '( 10 + 5 ) * 3 - 8 / 2'
# exec('print('+res.replace(' ', "")+')')



def brackets_remove(line):
    lst = []
    i = 0
    while i < len(line):
        if line[i] == '(':
            m = line.index(')', i)  # вернет индекс закрывающей скобки.
            # срез того, что в после и перед скобками.
            lst.append(line[i + 1:m])
            i = m
        else:  # аппендим по i
            lst.append(line[i])
        i += 1
    return lst
# [['10', '+', '5'], '*', '23', '-', '8']
# print(brackets_remove(res.split()))



def brackets_cont(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], list): #является ли экземпляром заданного класса/подкласса.
            a, b, c = brackets_remove(lst[i])
            lst[i] = actions[b](a, c) #() - дергаем лямбду.
    return lst
        
# print(brackets_cont(brackets_remove(res.split())))



def output(lst):
    prior = [i for i,j in enumerate(lst) if j in '*/'] # */ - будет проверять вхождение в строку.
    while prior:
        t = prior[0]
        a, b, c = lst[t - 1: t + 2]
        lst.insert(t - 1, actions[b](a, c))
        del lst[t: t + 3]
        prior = [i for i,j in enumerate(lst) if j in '*/']

    while len(lst) > 1:
        a, b, c = lst[:3]
        del lst[:3]
        lst.insert(0, actions[b](a, c))
        
    return lst

s2 = '2 - ( 2 + 7 ) * 2'
s3 = '4 * ( 3 - 1 ) / ( 9 - 7 )'

# print(output(brackets_cont(brackets_remove(res.split()))))
print(output(brackets_cont(brackets_remove(s3.split()))))
