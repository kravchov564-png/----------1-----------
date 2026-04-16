def obfuscator(func):
    """Декоратор для скрытия значений name и password в возвращаемом словаре"""

    def wrapper():
        # Получаем результат исходной функции
        result = func()

        # Обрабатываем ключ 'name' (скрываем все, кроме первого и последнего символа)
        if 'name' in result and isinstance(result['name'], str):
            name = result['name']
            if len(name) > 2:
                # Первый символ + звездочки (количество = длина - 2) + последний символ
                result['name'] = name[0] + '*' * (len(name) - 2) + name[-1]
            elif len(name) == 2:
                result['name'] = name[0] + '*'
            # если длина 1 или 0 - оставляем как есть

        # Обрабатываем ключ 'password' (все символы заменяем на звездочки)
        if 'password' in result and isinstance(result['password'], str):
            password = result['password']
            # Заменяем каждый символ на звездочку
            result['password'] = '*' * len(password)

        return result

    return wrapper


@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())
