from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import hi_command
from commands import time_command
from commands import help_command
from commands import sum_command



app = ApplicationBuilder().token("5721039212:AAGmlYkFN8G2_C5v0mLM3dIIzBp9v0Vihxw").build()



app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


print('server start')
app.run_polling()