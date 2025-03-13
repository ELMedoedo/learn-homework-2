"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

import datetime

def print_days():
    actual=datetime.datetime.today()

    delta_yest=datetime.timedelta(days=0)
    delta_month=datetime.timedelta(days=29)

    dt_yest=actual-delta_yest
    dt_month=actual-delta_month

    print(f"Cегодня: {actual.day}-{actual.month}-{actual.year}")
    print(f"Вчера: {dt_yest.day-1}-{dt_yest.month}-{dt_yest.year}")
    print(f"30 дней назад: {dt_month.day-1}-{dt_month.month}-{dt_month.year}")



def str_2_datetime(date_string):
    format="%d/%m/%y %H:%M:%S.%f"
    dt=datetime.datetime.strptime(date_string, format)
    return dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
