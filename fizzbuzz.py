def print_pack_report(starting_value):
    # Объявите диапазон от starting_value до 1 включительно
    # и переберите его в цикле:
    for number in range(starting_value, 0, -1):
        # Проверьте, делится ли текущий элемент
        # на 3, на 5 и на 3 и 5 одновременно.
        if number % 3 == 0 and number % 5 == 0:
            print(number, '- расфасуем по 3 или по 5')
        # В зависимости от результата проверки
        # напечатайте нужную фразу
        elif number % 5 == 0:
            print(number, '- расфасуем по 5')
        elif number % 3 == 0:
            print(number, '- расфасуем по 3')
        else:
            print(number, '- не заказываем!')


print_pack_report(6)