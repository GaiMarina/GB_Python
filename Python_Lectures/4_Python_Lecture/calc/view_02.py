
# Описываем модуль, который будет обеспечивать взаимодействие с пользователем.
# "Кнопочка, чтобы нажимать"

def view_data(data, title):     # Модель принимает какие-то данные и просто их выводит.
    print(f'{title} = {data}')

# Два модуля из model_sum.py нужно связать с методом ==> controller.py

def get_value():
    return int(input('value = '))