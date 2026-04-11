# Вместо многоточия укажите параметры num, leng и wid.
# Параметру wid присвойте значение по умолчанию.
def check_pool_capacity(num, leng, wid=None):
    # Проверьте параметр num на отрицательное значение.
    if num < 0:
        num = -num

    # Проверьте параметр leng на отрицательное значение.
    if leng < 0:
        leng = -leng

    # Проверьте значение параметра wid.
    if wid is not None and wid < 0:
        wid = -wid

    # Вычислите площадь бассейна и проверьте,
    # помещаются ли в бассейне все люди из очереди.
    # Верните True или False в зависимости от результата проверки.
    if wid is None:
        area = leng * leng
    else:
        area = leng * wid

    if area == 0:
        return False

    # помещаются ли в бассейне все люди из очереди.
    return num <= area * 2

# Код ниже полностью рабочий, он вам пригодится для проверки вашей работы.

# Функция, которая принимает на вход True или False
# и печатает текстовое сообщение.
def show_result(is_ok):
    if is_ok:  # Если передано True:
        print('Все люди из очереди поместятся в бассейн.')
    else:  # Если передано False:
        print('Люди из очереди не поместятся в бассейн.')


# Вызываем check_pool_capacity() с двумя аргументами.
# Этот вызов должен вернуть True (4 чел. в бассейн 2х2).
is_capacity_ok = check_pool_capacity(4, 2)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)

# Вызываем check_pool_capacity() с тремя аргументами.
# Этот вызов должен вернуть False (25 чел. в бассейн 5х2).
is_capacity_ok = check_pool_capacity(2, 2, 0)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)

# При необходимости добавьте свои вызовы аналогичным образом.