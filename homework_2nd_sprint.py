"""Модуль для обработки записей сотрудниках проверкой формата даты рождения."""

from datetime import datetime


def validate_record(name: str, birthdate: str) -> bool:
    """
    Проверяет корректность формата даты рождения.

    Args:
        name: Имя сотрудника
        birthdate: Дата рождения в виде строки

    Returns:
        bool: True, если дата соответствует формату ДД.ММ.ГГГГ, иначе False

    Prints:
        Сообщение об ошибке, если формат даты некорректный
    """
    try:
        datetime.strptime(birthdate, '%d.%m.%Y')
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False


def process_people(entries: list[tuple]) -> dict:
    """
    Подсчитывает количество корректных и некорректных записей.

    Args:
        entries: Список кортежей, где каждый кортеж содержит (имя, дата)

    Returns:
        dict: Словарь с ключами 'good' и 'bad', содержащий количество
              корректных и некорректных записей соответственно
    """
    good_count = 0
    bad_count = 0

    for name, birthdate in entries:
        if validate_record(name, birthdate):
            good_count += 1
        else:
            bad_count += 1

    return {'good': good_count, 'bad': bad_count}


data = [
    ('Акакій Башмачкинъ',    '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
]

statistics = process_people(data)
print(f'Корректных записей: {statistics["good"]}')
print(f'Некорректных записей: {statistics["bad"]}')
