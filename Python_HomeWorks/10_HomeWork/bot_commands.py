import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler, CallbackContext, CallbackQueryHandler,
)

from pipPy.infa import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TYPE_NUMS_CHOICE, EXPRESSION_INPUT, FLOAT_CALCULATIONS, COMPLEX_CALCULATIONS = range(4)


def space_grouping(exp):
    l_ist = ''
    for i in exp:
        if i == '.' or i == ',':
            i = '.'
            l_ist = l_ist[:-1]
            l_ist += i
            continue
        elif i:
            l_ist += i
            l_ist += ' '
    return l_ist


def rearrangement(update, exp_msg):
    user = update.message.from_user
    input_list = exp_msg.split()  # Промежуточный output (4', '3', '1', '-', '*', '9', '7', '-', '/')
    output = []
    stack_list = []
    for elem in input_list:  # '4*(3-1)/(9-7)'
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


def start(update, _):
    reply_keyboard = [['start', 'help', 'exit']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("Hello, I'm a calculator_bot! Use the tips below to go on.",
                              reply_markup=markup_key)
    return TYPE_NUMS_CHOICE


def type_nums_choice(update, _):
    reply_keyboard = [['complex', 'float']]
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's choice: %s: %s", user.first_name, msg)
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text("Ok, make your choice: ",
                              reply_markup=markup_key)
    return EXPRESSION_INPUT


def expression_input(update, _):
    msg = update.message.text
    # update.message.reply_text(msg)  # float
    user = update.message.from_user
    logger.info("User's choice: %s: %s", user.first_name, msg)
    update.message.reply_text('Input an expression to calculate: ')
    if msg == 'float':
        return FLOAT_CALCULATIONS
    elif msg == 'complex':
        return COMPLEX_CALCULATIONS


def float_calculations(update, context: CallbackContext):
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's expression: %s: %s", user.first_name, msg)
    lst = space_grouping(msg)
    arr_lst = rearrangement(update, lst)
    update.message.reply_text(arr_lst)  # ["5.6", "8.2", "+", "1", "-"]
    calc(arr_lst)
    update.message.reply_text(f'{msg} = {calc(arr_lst)}')
    return cancel


def complex_calculations(update, _):
    user = update.message.from_user
    msg = update.message.text
    logger.info("User's input: %s: %s", user.first_name, msg)
    update.message.reply_text(msg)
    return ConversationHandler.END


def cancel(update, _):
    update.message.reply_text('Bye')
    return ConversationHandler.END


# ================================

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            TYPE_NUMS_CHOICE: [MessageHandler(Filters.regex('^(start|help|exit)$'), type_nums_choice)],
            # COMPLEX_OP: [MessageHandler(Filters.regex('^(complex|float)$'), complex_op)],
            EXPRESSION_INPUT: [MessageHandler(Filters.regex('^(complex|float)$'), expression_input)],
            FLOAT_CALCULATIONS: [MessageHandler(Filters.text, float_calculations)],
            COMPLEX_CALCULATIONS: [MessageHandler(Filters.text, complex_calculations)],
            # CHOICE: [MessageHandler(Filters.text, choice)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()

# =============================================
