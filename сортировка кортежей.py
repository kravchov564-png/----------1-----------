apple_tree_yields = (150, 210, 90, 120, 140, 190, 130, 150, 110, 200, 150)

# Функция reversed_sort() должна принять на вход кортеж
# и вернуть кортеж с теми же элементами, отсортированными по убыванию.
def reversed_sort(apple_tree_yields):
    apple_tree_yields = sorted(apple_tree_yields)
    apple_tree_yields = sorted(apple_tree_yields, reverse=True)
    apple_tree_yields = tuple(apple_tree_yields)
    return apple_tree_yields
    # 1. К полученному кортежу примените функцию сортировки;
    # затем результат сортировки преобразуйте в кортеж и верните.


# Присвойте переменной result результат
# вызова функции reversed_sort() с аргументом apple_tree_yields.
result = reversed_sort(apple_tree_yields)
# Напечатайте:
print(result[0])  # наибольшее значение из кортежа result,
print(result[1])  # второе по величине значение из кортежа result,
print(result[2])  # третье по величине значение из кортежа result.