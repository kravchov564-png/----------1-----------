from datetime import datetime
from random import sample


def choose_days():
    # Определяем диапазон дат первой половины месяца.
    first_month_half = list(range(1, 16))  # Исправлено: дни с 1 по 15

    # Выбор трёх случайных чисел:
    random_days = sample(first_month_half, k=3)
    # Cортировка этих чисел по возрастанию:
    sorted_days = sorted(random_days)

    # Получаем сегодняшнюю дату.
    # На её основе будут генерироваться даты для занятий:
    now = datetime.now()

    # Цикл для трёх занятий
    for i in range(3):  # Индексы 0, 1, 2
        # Генерируем дату занятия
        practice_day = now.replace(day=sorted_days[i]).strftime(
            "%d.%m.%Y")  # Исправлено: %M на %m (минуты на месяцы)
        print(f'{i+1}-е занятие: {practice_day}')


choose_days()
