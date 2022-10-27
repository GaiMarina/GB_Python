from logging import log
from random import randint


from telegram import Update
from telegram.ext import (ConversationHandler, CallbackContext)
from telegram import update


def move_making(mode, name, candies_left):
    q = 0
    while not q:
        if mode == 'PC' or mode == 'game_bot':
            q = update.message.reply_text(f'{update.message.chat.first_name}! Enter the number of candies to take from 1 to 28: ')
            if q.isdigit and int(q) in range(1, 29):
                q = int(q)
            else:
                q = 0
                print(f"Invalid input! Try again!")
        elif mode == 'PC':
            q = randint(1, 29)
        else:
            q = candies_left % 29
            if q <= 0:
                q = 1
    return q


def print_result(candies, player, cans_take):
    update.message.reply_text(f'{cans_take} taken by the {player}')
    update.message.reply_text(f'{candies} of the candies left.')


def cancel(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        "It's a pity that you refused. "
        "Any time you are boring, we can play.")
    # Заканчиваем разговор.
    return ConversationHandler.END

def help_command(update, _):
    update.message.reply_text("Input `/start` for beggining.")

# шаблон для построения кнопок
def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

    # def button(update):
    #     query = update.callback_query
    #     variant = query.data
    #     # `CallbackQueries` требует ответа, даже если
    #     # уведомление для пользователя не требуется, в противном
    #     query.answer()
    #     # редактируем сообщение, тем самым кнопки
    #     # в чате заменятся на этот ответ.
    #     query.edit_message_text(f"Your choice is: {variant}")