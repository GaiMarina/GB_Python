from datetime import datetime

FILE_NAME = "calc_log.csv"

def write_log(num1, num2, operation, result):
    with open(FILE_NAME, "a", encoding="UTF-8") as f:
        f.write(f"{datetime.now().strftime('%d.%m.%Y %H:%M')} Введены числа: {num1}, {num2}. Операция {operation}. Результат {result}\n")


def read_log():
    with open(FILE_NAME, "r", encoding="UTF-8") as f: 
        print(f.read())
