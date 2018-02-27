import locale
from datetime import datetime, timedelta

locale.setlocale(locale.LC_ALL, "russian")

date_now = datetime.now()
date_yesterday = date_now - timedelta(days=1)
date_month_ago = date_now - timedelta(days=30)

print('''Время сейчас: {0} \n
        Вчера: {1} \n
        Месяц назад: {2} \n'''.format(date_now, date_yesterday, date_month_ago))

date_string = "01/01/17 12:10:03.234567"
date_formatted = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_formatted, type(date_formatted))
