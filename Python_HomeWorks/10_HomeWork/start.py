from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_commands import *
from pipPy.infa import TOKEN

if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancel))


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      CommandHandler('help', help_command),
                      CommandHandler('cancel', cancel)],
        states={
            TYPE_NUMS_CHOICE: [MessageHandler(Filters.regex("^(Let's start!)$"), type_nums_choice),
                               CommandHandler('start', start),
                               CommandHandler('help', help_command),
                               CommandHandler('cancel', cancel)
                               ],
            EXPRESSION_INPUT: [MessageHandler(Filters.regex('^(complex|float)$'), expression_input),
                               CommandHandler('help', help_command),
                               CommandHandler('cancel', cancel),
                               CommandHandler('start', start)
                               ],
            FLOAT_CALCULATIONS: [MessageHandler(Filters.text, float_calculations),
                                 CommandHandler('help', help_command),
                                 CommandHandler('cancel', cancel),
                                 CommandHandler('start', start)
                                 ],
            COMPLEX_CALCULATIONS: [MessageHandler(Filters.text, complex_calculations),
                                   CommandHandler('help', help_command),
                                   CommandHandler('cancel', cancel),
                                   CommandHandler('start', start)
                                   ],
        },
        fallbacks=[CommandHandler('cancel', cancel),
                   CommandHandler('help', help_command),
                   CommandHandler('start', start)
                   ]
    )



    dispatcher.add_handler(conv_handler)

    print('server start')

    updater.start_polling()
    updater.idle()
