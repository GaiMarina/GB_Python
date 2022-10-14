
# Написать систему, которая собирает информацию с датчиков, в ней есть модуль логирования, который заносит в журнал
# все обращения к датчикам.
# В системе есть модуль, выполняющий обращения для получения данных с датчиков и модуль генерации html-представления.
# Запуск системы осуществляется из головного модуля.

# 1. Сбор информации с датчиков     data_provider           get_temperature, get_pressure, get_wind_speed
# 2. логирование                    logger                  temperature_logger, pressure_logger, wind_speed_logger
# 3. UA                             user_interface          temperature_view, pressure_view, wind_speed_view
# 4. HTML-генератор                 html_creater            create
# 5. Главный модуль.                main                    кнопка: запустить систему.

# Поставляет данные.

from cgitb import html
import imp
from random import randint

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)


def get_preassure(sensor):
    if sensor:
        return randint(720, 750)
    else:
        return randint(750, 770)


def get_wind_speed(sensor):
    if sensor == 1:
        return randint(0, 30)
    else:
        return randint(30, 50)

def data_collection(sensor = 1):
    return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))

