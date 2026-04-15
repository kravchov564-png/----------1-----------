class Employee:
    vacation_days: int = 28

    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days
        self._employee_id = self.__generate_employee_id()

    def __generate_employee_id(self) -> int:
        """Приватный метод для генерации ID сотрудника"""
        string_for_hash = self.first_name + self.last_name + self.gender
        return hash(string_for_hash)

    def consume_vacation(self, days: int):
        self.remaining_vacation_days -= days

    def get_remaining_vacation_days(self) -> int:
        return self.remaining_vacation_days


class OfficeEmployee(Employee):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        gender: str,
        worker_class: int,
        salary: int
    ):

        super().__init__(first_name, last_name, gender)
        self.worker_class = worker_class
        self.__salary = salary

    def get_vacation_payment(self, vacation_days: int):
        self.vacation_days = vacation_days
        if self.worker_class == 1:
            self.vacation_days += 2
        elif self.worker_class == 2:
            self.vacation_days += 4
        elif self.worker_class == 3:
            self.vacation_days += 6
        elif self.worker_class == 4:
            self.vacation_days += 8
        return int((self.__salary / 60) * vacation_days)


# Пример использования:
office_employee = OfficeEmployee(
    first_name='Иван',
    last_name='Иванов',
    gender='м',
    worker_class=2,
    salary=45000
)

vacation_days = 10

office_employee.consume_vacation(vacation_days)

remaining_days = office_employee.get_remaining_vacation_days()
print(f'У сотрудника осталось {remaining_days} дн. отпуска.')

vacation_payment = office_employee.get_vacation_payment(vacation_days)
print(f'За {vacation_days} дн. отпуска сотрудник получит {vacation_payment} руб.')
