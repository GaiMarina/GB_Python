
import info_input as info
from datetime import datetime

# Внес запись в логи в формате csv: дата, время, запись.

FILE_NAME = 'phone_book.csv'

def log_input(entry):
    with open(FILE_NAME, 'a', encoding='UTF-8') as rec:
        rec.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M')} {entry} \n")

