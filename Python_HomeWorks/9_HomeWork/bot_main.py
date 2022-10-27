import logging
from random import randint
from infa.infa import TOKEN
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()

global first_name
global mode
global all_the_candies

def start(update: Update, context: CallbackContext):
    log(update, context)

    update.message.reply_text(f"Hi! I'm a game_bot. Will you play with me?\n\n"
                              "The game with candies. \n"
                              "You will choose the total number of candies for the game. "
                              "Any time when it's your turn, you can take from 1 to 28 candies. "
                              "If you manage to leave the PC or the game_bot without any candies you win. \n\n"
                              "Press '/toss_up' define who's turn will be the first.")
    # reply_markup=reply_markup)


def toss_up(update: Update, context: CallbackContext):
    log(update, context)
    toss_up = randint(0, 1)
    if toss_up:
        update.message.reply_text(f'PC or game_bot will make the first move.\n\n')
        mode = 'PC'
    else:
        update.message.reply_text(f'You are making the first move.\n\n')
        mode = 'person'
    update.message.reply_text(f"Print /all_candies to input the total number of candies for the play.")


def all_candies(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Input the total number of candies for the play.")
    all_the_candies = update.message.text
    update.message.reply_text(all_the_candies)


# def pc_play(update: Update, context: CallbackContext):
#     log(update, context)
#
#     if mode == 'PC':
#         first_player  = 'PC'
#         second_player = first_name
#         while all_the_candies > 28:
#             cands_taken = randint(1, 28)
#             update.message.reply_text(f'The total amount of candies equals {all_the_candies}.\n'
#                                       f'{first_player} took {cands_taken} of candies.')
#             all_the_candies -= cands_taken
#             if all_the_candies == 0:
#                 update.message.reply_text(f'{first_player} is a winner! Try again!')
#             else:
#                 update.message.reply_text(f'The total amount of candies equals {all_the_candies}\n'
#                                           f'How many candies from 1 to 28 will you take?')
#                 cands_taken = update.message.text
#                 all_the_candies -= cands_taken
#                 if all_the_candies == 0:
#                     update.message.reply_text(f'{second_player} is a winner! Try again!')
#
#     else:
#         first_player = first_name
#         second_player = 'PC'
#         while all_the_candies  > 28:
#             update.message.reply_text(f'The total amount of candies equals {all_the_candies}\n'
#                                       f'How many candies from 1 to 28 will you take?')
#             cands_taken = update.message.text
#             all_the_candies -= cands_taken
#             cands_taken = randint(1, 29)
#             update.message.reply_text(f'The total amount of candies equals {all_the_candies}.\n'
#                                       f'{second_player} took {cands_taken} of candies.')
#             all_the_candies -= cands_taken


        # else:
        #     update.message.reply_text(f'Congratulations! You win!')

# def game_bot_play
#
#             q = 0
#             while not q:
#                 if mode == 'PC' or mode == 'game_bot':
#                     q = update.message.reply_text(
#                         f'{update.message.chat.first_name}! Enter the number of candies to take from 1 to 28: ')
#                     if q.isdigit and int(q) in range(1, 29):
#                         q = int(q)
#                     else:
#                         q = 0
#                         print(f"Invalid input! Try again!")
#                 elif mode == 'PC':
#                     q = randint(1, 29)
#                 else:
#                     q = candies_left % 29
#                     if q <= 0:
#                         q = 1
#             return q
#
#         candies_taken = move_making(game_mode_select,
#                                     first_plr if toss_up else second_plr,
#                                     all_the_candies)
#         all_the_candies -= candies_taken
#         print_result(all_the_candies, first_plr if toss_up else second_plr, candies_taken)
#         toss_up = not toss_up
#     update.message.reply_text(f'Congratulations! {first_plr if toss_up else second_plr} is a winner!')

# ====================================================

if __name__ == '__main__':

    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('toss_up', toss_up))
    updater.dispatcher.add_handler(CommandHandler('all_candies', all_candies))
    # updater.dispatcher.add_handler(CommandHandler('PC', pc_play))
    # updater.dispatcher.add_handler(CommandHandler('w_d', w_d_command))
    # updater.dispatcher.add_handler(CommandHandler('ran', ran_command))

    updater.start_polling()
    updater.idle()

# ===================================
