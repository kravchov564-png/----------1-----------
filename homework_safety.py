"""
Модуль для работы с пользователями и их конфиденциальными данными.
Содержит класс User и декоратор obfuscator для скрытия информации.
"""


class User:
    """
    Класс, представляющий пользователя социальной сети.

    Позволяет создавать пользователей с именем/фамилией или псевдонимом,
    а также получать форматированное полное имя.
    """

    def __init__(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            username: str | None = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    @classmethod
    def with_name(cls, first_name: str, last_name: str):
        """Создает пользователя с указанными именем и фамилией."""
        return cls(first_name=first_name, last_name=last_name)

    @classmethod
    def with_username(cls, username: str):
        """Создает пользователя с псевдонимом после проверки."""
        if not cls.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        return cls(username=username)

    @staticmethod
    def is_username_allowed(username: str) -> bool:
        """Проверяет, разрешен ли псевдоним(не должен начинаться с 'admin')."""
        return not username.startswith('admin')

    @property
    def full_name(self) -> str:
        """Возвращает полное имя пользователя или псевдоним с @."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.username:
            return f"@{self.username}"
        return ""


def obfuscator(func):
    """
    Декоратор для скрытия конфиденциальных данных.

    Скрывает значение ключа 'name' (оставляя первый и последний символы)
    и полностью маскирует значение ключа 'password'.
    """
    def wrapper():
        result = func()

        if 'name' in result and isinstance(result['name'], str):
            name = result['name']
            if len(name) > 2:
                result['name'] = name[0] + '*' * (len(name) - 2) + name[-1]
            elif len(name) == 2:
                result['name'] = name[0] + '*'

        if 'password' in result and isinstance(result['password'], str):
            password = result['password']
            result['password'] = '*' * len(password)

        return result
    return wrapper


@obfuscator
def get_credentials():
    """Возвращает словарь с учетными данными пользователя."""
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


if __name__ == '__main__':
    stas = User.with_name('Стас', 'Басов')
    print(stas.full_name)

    credentials = get_credentials()
    print(credentials)
