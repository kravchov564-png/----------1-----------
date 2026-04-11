def find_common_words_count(first_string, second_string):

    # Преобразуйте строки в списки, разбив их по пробелам.
    list(first_string.split(' '))
    list(second_string.split(' '))

    # Преобразуйте полученные списки в множества
    set1 = set(first_string.split(' '))
    set2 = set(second_string.split(' '))
    # (элементами множества будут только уникальные значения из списка).
    # Получите пересечение двух множеств - это будет новая коллекция.
    common_words_count = len(set1.intersection(set2))
    return common_words_count

    # Верните длину получившейся коллекции.


phrase_1 = 'кот зол как лев дай мне сыр дай мне суп'
phrase_2 = 'кто ест сыр тот кот кто ест суп тот нет'

common_words_count = find_common_words_count(phrase_1, phrase_2)
print('Общих уникальных слов в предложениях:', common_words_count)