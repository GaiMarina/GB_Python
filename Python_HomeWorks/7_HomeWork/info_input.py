# 1. Собрал данные, сделал запись.

def data_input():
    name = input('Input the name: ')
    patronymic = input('Input the patronymic: ')
    surname = input('Input the surname: ')
    ph_num = input('Input the phone number: ')
    comment = input('Input any additional  information to keep: ')
    one_entry = [surname, name, patronymic, ph_num, comment]
    return one_entry
