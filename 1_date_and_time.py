

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date,time,datetime,timedelta

def print_days():
    now = datetime.now().strftime("%d/%m/%Y")
    yesterday =  (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
    month_ago = (datetime.now() - timedelta(days=30)).strftime("%d/%m/%Y")
    print( now, yesterday, month_ago, sep='\n')


def str_2_datetime(date_string):
    return type(datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f'))

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
