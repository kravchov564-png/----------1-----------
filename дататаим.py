# Импортируйте тип datetime.
from datetime import datetime, timedelta
from email.utils import format_datetime


def get_difference_in_days(datetime_str_1, datetime_str_2):

    format_datetime= '%Y/%m/%d %H:%M:%S'

    date1 = datetime.strptime(datetime_str_1, format_datetime)
    date2 = datetime.strptime(datetime_str_2, format_datetime)

    difference = date2 - date1

    return difference.days


# Преобразуйте полученные в качестве аргументов функции строки
# в тип datetime по нужному шаблону.
# Вычислите разницу между двумя датами (получится тип timedelta)
# и верните количество целых дней.


difference = get_difference_in_days('2019/05/10 11:26:31', '2019/10/04 10:01:19')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')