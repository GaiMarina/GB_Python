from input_data import input_number, input_operation
from calc_op import calc_sum, calc_div, calc_mult, calc_sub
from calc_logging import write_log


def calculation():
    a = input_number()
    b = input_number()
    op = input_operation()
    if op == "1":
        res = calc_sum(a, b)
    elif op == "2":
        res = calc_sub(a, b)
    elif op == "3":
        res = calc_mult(a, b)
    elif op == "4": 
        res = calc_div(a, b)
    print(res)
    write_log(a, b, op, res)
