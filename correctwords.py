# Код этой функции не меняйте.
def count_tiles(dep, leng, wid=None):
    if wid is None:
        wid = leng

    short_sides = 2 * wid * dep
    long_sides = 2 * leng * dep
    bottom = leng * wid
    total = short_sides + long_sides + bottom

    return total


# Допишите код функции.
def make_word(count):
    if count != 11 and count % 10 == 1 :
        return 'плитка'
    elif 5<=count<=20:      # Блоков elif может быть сколько угодно.
        return 'плиток'
    elif count % 10 == 2 or count % 10 == 3 or count % 10 == 4:
        return 'плитки'
    elif count == 1:
        return 'плитка'
    else:
        return 'плиток'


# Вычисляем количество плиток:
total_tiles = count_tiles(1, 1, 1)

# Полученное число передаём в make_word(),
# чтобы подобрать нужное склонение для слова "плитка":
correct_word = make_word(total_tiles)

# Печатаем итоговую фразу, в которой применяем число плиток total_tiles
# и слово "плитка" в правильном склонении (correct_word):
print('Потребуется', total_tiles, correct_word)