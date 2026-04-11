def get_selection(collection):
    # Напишите код функции.
    new_collection = collection[1:-1]

    return new_collection  # Верните требуемый список.


heights = [140.1, 150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1, 180]
selection = get_selection(heights)
print('Выборка:', selection)

# Ожидаемый вывод на печать:
# Выборка: [150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1]