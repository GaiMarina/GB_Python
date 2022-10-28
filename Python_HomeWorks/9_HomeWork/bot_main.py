import logging
from random import randint

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from pipPy.infa import TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()


def start(update: Update, context: CallbackContext):
    log(update, context)

    update.message.reply_text("************************************\n"
                              "Hi! I'm a game_bot. Will you play with me?\n"
                              "************************************\n\n"
                              "---------------------------------------------------------------\n"
                              "🍬🍬🍬 The game with candies 🍬🍬🍬 \n"
                              "---------------------------------------------------------------\n\n"
                              "You will choose the total number of candies for the game. "
                              "Any time when it's your turn, you can take from 1 to 28 candies. "
                              "If you manage to leave the PC or the game_bot without any candies, you win. \n\n"
                              "Press /toss_up to define whose turn will be the first."
                              "Any time you can press /cancel to exit.")


def toss_up(update: Update, context: CallbackContext):
    log(update, context)
    tossup = randint(0, 1)
    if tossup:
        update.message.reply_text(f"PC or game_bot will make the first move.\n"
                                  f"-----------------------------------------------------------\n"
                                  f"Press '/', PC or game_bot, space and the total number of candies for the game"
                                  f" to pass the turn.\n"
                                  f"(Ex.: /PC 87)\n"
                                  f"(Ex.: /game_bot 87).")
    else:
        update.message.reply_text("You are making the first move.😎\n"
                                  "--------------------------------------------\n"
                                  "Print '/', 'me', then space, then the total number of candies for the game, "
                                  "then space and the number of candies to take (from 1 to 28) to make your move.\n"
                                  "(Ex.: /me 87 24).")


def me(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    b = int(items[2])
    if a <= b:
        update.message.reply_text(f"Congratulations!!! You win!!!🥳🥳🥳")
    else:
        update.message.reply_text("The total number of candies equals: "
                                  f"{a - b}\n\n"
                                  f"Press '/', PC or game_bot, space and {a - b} then, to pass the turn.")


def pc(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    b = randint(1, 29)
    if a <= b:
        update.message.reply_text("PC is a winner! Press /start to try again!")
    else:
        update.message.reply_text(f"PC took {b} candies.\n"
                                  f"The total number of candies equals: {a - b}\n\n"
                                  f"Print '/', 'me', then space, then {a - b}, then space"
                                  " and the number of candies to take (from 1 to 28) to make your move.\n"
                                  "(Ex.: /me 87 24).")


def game_bot(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    b = a % 29
    if b == 0:
        b = 1
    if a <= b:
        update.message.reply_text(f"Game_bot is a winner! Press /start to try again!")
    else:
        update.message.reply_text(f"game_bot took {b} candies.\n"
                                  f"The total number of candies equals: {a - b}\n\n"
                                  f"Print '/', 'me', then space, then {a - b}, then space"
                                  " and the number of candies to take (from 1 to 28) to make your move.\n"
                                  "(Ex.: /me 87 24).")


def cancel(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f"Sorry that you stopped to play. I'll be glad to see you the next time")


# ====================================================

if __name__ == '__main__':
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('toss_up', toss_up))
    updater.dispatcher.add_handler(CommandHandler('me', me))
    updater.dispatcher.add_handler(CommandHandler('PC', pc))
    updater.dispatcher.add_handler(CommandHandler('game_bot', game_bot))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancel))

    updater.start_polling()
    updater.idle()

# ======================================================
