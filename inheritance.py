"""Модуль для работы с сотрудниками и отпусками."""

from datetime import datetime


class Employee:
    """Базовый класс для всех сотрудников."""

    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        """Инициализация сотрудника."""
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        """Списать отпускные дни."""
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        """Вернуть информацию об остатке отпускных дней."""
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):
    """Класс для сотрудентов на полный рабочий день."""

    def get_unpaid_vacation(self, start_date, days):
        """
        Рассчитать неоплачиваемый отпуск.

        Args:
            start_date: Дата начала отпуска в формате ГГГГ-ММ-ДД.
            days: Продолжительность отпуска в днях.

        Returns:
            str: Информация о неоплачиваемом отпуске.
        """
        # Преобразуем строку в объект datetime
        date = datetime.strptime(start_date, '%Y-%m-%d')
        # Форматируем дату в нужный формат
        formatted_date = date.strftime('%Y/%m/%d')
        return (f'Начало неоплаченного отпуска: {formatted_date}, '
                f'продолжительность: {days} дней.')


class PartTimeEmployee(Employee):
    """Класс для сотрудников на неполный рабочий день."""

    vacation_days = 14


# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())
