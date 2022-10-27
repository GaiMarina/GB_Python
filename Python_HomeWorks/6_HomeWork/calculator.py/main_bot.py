
from statistics import mode
import model_sub as model
from statistics import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.sum()
    view.view_data(result, "resul")