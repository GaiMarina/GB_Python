
from curses.ascii import isalpha


# 1. Собрал данные, сделал запись.

def data_input():
    name = input('Input the name: ')
    patronymic = input('Input the pantronimic: ')
    surname = input('Input the surname: ')
    ph_num = input('Input the phone number: ')
    comment = input('Input any additional  information to keep: ')
    one_entry = f'{name} {patronymic} {surname} {ph_num} {comment}'
    return one_entry
