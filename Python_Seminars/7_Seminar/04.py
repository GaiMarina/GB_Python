
# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
#      возвращает словарь, ключи — первые буквы фамилий, значения — словари,
#      реализованные по схеме предыдущего задания.

def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:                    # Из фамилии с индексом [1] берем 1-ю букву с индексом [0]
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return s_n_sort
# setdefault() если нет значения, возвращает None, в нашем случает {} и к нему опять .setdefault().
#                     [0]   [1]
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                    "Борис Аркадьев", "Антон Серов", "Павел Анисимов"))
