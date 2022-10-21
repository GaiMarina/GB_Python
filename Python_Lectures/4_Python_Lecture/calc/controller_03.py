

import model_mult_05 as mult # импортируем модуль из файла, который сами создали.
import view_02

def button_click():                 # получение данных из консоли: одно число и второе число.
    value_a = view_02.get_value()      # get_value - описываем во view
    value_b = view_02.get_value()  
    mult.init(value_a, value_b)    # инициализируем входные данные, 
    result = mult.do_it()            # передав соотв-щие аргументы, перемножаем.
    view_02.view_data(result, 'multiplation equals') # возвращаем значение во view