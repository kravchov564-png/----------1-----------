fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.
# Объявляем новый список, в него будем складывать изменённые значения.
corrected_fruit_yields = []

# Объявите цикл, в нём переберите список fruit_yields.
for i in range(len(fruit_yields)):
# В теле цикла к каждому значению списка добавьте 1.2,
    corrected_fruit_yields.append(fruit_yields[i] + 1.2)
# затем получившееся значение сохраните в список corrected_fruit_yields.

# Чтобы увидеть, что получилось,
# напечатаем список с откорректированными значениями.
print(corrected_fruit_yields)

#===================================================================================================2 способ
fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.

# Вместо всего этого кода нужно написать единственную строчку,
# которая выполнит те же действия.
# corrected_fruit_yields = []

# for yield_value in fruit_yields:
#     yield_value += 1.2
#     list.append(corrected_fruit_yields, yield_value)

corrected_fruit_yields = [value + 1.2 for value in fruit_yields]  # Ваш код - здесь.

print(corrected_fruit_yields)