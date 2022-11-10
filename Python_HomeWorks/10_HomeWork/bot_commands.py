import logging
from lib2to3.fixes.fix_input import context

from logs import log
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ConversationHandler, CallbackContext)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TYPE_NUMS_CHOICE, EXPRESSION_INPUT, FLOAT_CALCULATIONS, COMPLEX_CALCULATIONS = range(4)


def space_grouping(exp):
    l_ist = ''
    for i in exp:
        if i.isdigit():
            l_ist += i
        elif i == '.' or i == ',':
            i = '.'
            l_ist += i
            continue
        elif i in ["*", "/", "-", "+", "(", ")"]:
            l_ist += ' ' + i + ' '
    return l_ist


def rearrangement(update, exp_msg):
    user = update.message.from_user
    input_list = exp_msg.split()
    output = []
    stack_list = []
    for elem in input_list:
        if elem[0].isdigit():  # цифры в output
            output.append(
                elem)  # ['4']  # ['*', '(']  # ['4', '3']  # ['4', '3', '1'] # ['/', '('] # ['4', '3', '1', '-', '*', '9']
        elif elem == "(":  # помещаем в стек (первый вошел, последний вышел) открывающую скобку в stack_list
            stack_list.append(elem)  # ['*', '(']  # ['/', '(']
        elif elem == ")":  # аппендим то, что до закрывающей скобки в output: знак
            while stack_list and stack_list[-1] != "(":
                output.append(stack_list.pop())  # забираем последний элемент из stack и помещаем знак в output
                # print(output)  # ['4', '3', '1', '-']  # ['4', '3', '1', '-', '*', '9', '7', '-']
            if not stack_list:
                logger.info("Error! %s: %s", user.first_name, "Несогласованные скобки")
                update.message.reply_text("Uncorrect placement of parentheses")
                exit()
            stack_list.pop()  # ['*'] # ['/']
        elif elem in ["*", "/"]:
            while stack_list and stack_list[-1] in ["*", "/"]:
                output.append(stack_list.pop())  # ['4', '3', '1', '-', '*']
            stack_list.append(elem)  # ['*']  # ['/']
        elif elem in ["+", "-"]:
            while stack_list and stack_list[-1] in ["*", "/", "+", "-"]:
                output.append(stack_list.pop())
            stack_list.append(elem)  # ['*', '(', '-']  # ['/', '(', '-']
        else:
            logger.info("Error! %s: %s", user.first_name, 'Нераспознанный знак')
            update.message.reply_text("Error! Unrecognized sign!")
            exit()
    while stack_list:
        if stack_list[-1] not in ["*", "/", "+", "-"]:
            logger.info("Error! %s: %s", user.first_name, "Несогласованные скобки")
            update.message.reply_text("Uncorrect placement of parentheses")
            exit()
        output.append(stack_list.pop())  # ['4', '3', '1', '-', '*', '9', '7', '-', '/']
    return output


def calc(out):
    res = []
    for elem in out:  # ['4', '3.2', '1', '-', '*', '9', '7', '-', '/']
        if elem[0].isdigit():
            res.append(float(elem))  # [4]  # [4, 3]  # [4, 3, 1]  # [8, 9]  # [8, 9, 7]
        else:
            b = res.pop()
            a = res.pop()  # 3 1  # 4 2  # 9 7  # 8 2
            if elem == "+":
                res.append(a + b)
            elif elem == "-":
                res.append(a - b)  # [4, 2]  # [8, 2]
            elif elem == "*":
                res.append(a * b)  # 4 2
            elif elem == "/":
                res.append(a / b)  # 8 2
    return res[0]


def calc_complex(out):
    res = []
    for elem in out:  # ['4', '3.2', '1', '-', '*', '9', '7', '-', '/']
        if elem[0].isdigit():
            for j in elem:
                if j.isdigit():
                    float(j)
            res.append(complex(elem))  # [4]  # [4, 3]  # [4, 3, 1]  # [8, 9]  # [8, 9, 7]
        else:
            b = res.pop()
            a = res.pop()  # 3 1  # 4 2  # 9 7  # 8 2
            if elem == "+":
                res.append(a + b)
            elif elem == "-":
                res.append(a - b)  # [4, 2]  # [8, 2]
            elif elem == "*":
                res.append(a * b)  # 4 2
            elif elem == "/":
                res.append(a / b)  # 8 2
    return res[0]


def help_command(update, context: CallbackContext):
    update.message.reply_text("CALCULATOR PROGRAM \n"
                              "/start allows you to start from the beginning \n"
                              "/cancel is to quit \n\n"
                              "In mode 'FLOAT' an expression is entered as a whole\n"
                              "Ex: 3-2.3+(4-5)\n\n"
                              "In mode 'COMPLEX' the complex numbers must be entered without "
                              "any spaces. "
                              "All the other numbers and marks must be entered with a space.\n"
                              "Ex: 2-3j + 5-4j")


def start(update, _):
    log(update, context)
    reply_keyboard = [["Let's start!"]]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Hello, I'm a calculator_bot! \n\n"
                              "In mode 'FLOAT' an expression is entered as a whole\n" \
                              "Ex: 3-2.3+(4-5)\n\n"
                              "In mode 'COMPLEX' the complex numbers must be entered "
                              "without any spaces. " \
                              "All the other numbers and marks must be entered with a space.\n" \
                              "Ex: 2-3j + 5-4j\n\n"
                              "Press /start to restart\n"
                              "press /help for an information\n"
                              "or press /cancel to quit\n\n"
                              "Use the tips below to go on.", reply_markup=markup_key)
    return TYPE_NUMS_CHOICE


def type_nums_choice(update, _):
    log(update, context)
    reply_keyboard = [['complex', 'float']]
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's choice: %s: %s", user.first_name, msg)
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Ok, make your choice: \n"
                              "/start /help /cancel",
                              reply_markup=markup_key)
    return EXPRESSION_INPUT


def expression_input(update, _):
    log(update, context)
    msg = update.message.text
    user = update.message.from_user
    logger.info("User's choice: %s: %s", user.first_name, msg)
    update.message.reply_text('Input an expression to calculate: ')
    if msg == 'float':
        return FLOAT_CALCULATIONS
    elif msg == 'complex':
        return COMPLEX_CALCULATIONS


def float_calculations(update, context: CallbackContext):
    log(update, context)
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's expression: %s: %s", user.first_name, msg)
    lst = space_grouping(msg)
    arr_lst = rearrangement(update, lst)
    calc(arr_lst)
    update.message.reply_text(f'{msg} = {calc(arr_lst)}\n\n'
                              f'/start /help /cancel')
    return cancel


def complex_calculations(update, context):
    log(update, context)
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's input: %s: %s", user.first_name, msg)
    lst = rearrangement(update, msg)
    update.message.reply_text(f'{calc_complex(lst)}\n\n'
                              f'/start /help /cancel')
    return ConversationHandler.END


def cancel(update, _):
    log(update, context)
    update.message.reply_text('Bye \n\n'
                              '/start /help /cancel', reply_markup=ReplyKeyboardRemove())

