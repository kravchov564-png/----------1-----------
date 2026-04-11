# Вместо многоточия укажите необходимые параметры.
def count_tiles(dep, leng, wid = None):
    # Опишите условие для случая, когда ширина бассейна не указана.
    if wid == None:
        wid = leng

    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
    all_tiles = leng * wid + 2 * (leng +  wid) * dep
    return all_tiles

    # Верните результат работы функции.
    return leng and all_tiles

total_tiles_1 = count_tiles(2, 2)
print('Потребуется плиток:', total_tiles_1)
# Должно быть напечатано: Потребуется плиток: 20

total_tiles_2 = count_tiles(1, 2, 3)
print('Потребуется плиток:', total_tiles_2)
# Должно быть напечатано: Потребуется плиток: 16

total_tiles_3 = count_tiles(2, 5, 3)
print('Потребуется плиток:', total_tiles_3)
# Должно быть напечатано: Потребуется плиток: 47