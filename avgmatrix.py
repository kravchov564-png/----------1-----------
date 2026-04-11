# Пригодится для наполнения списков!
import random

# 1. Создание списка списков:
rows = 3
cols = 3
#print(garden_rows)
#print(garden_cols)
harvest = [[random.randint(5,20) for _ in range(cols)] for _ in range(rows)]  # Примените list comprehension.
#print(harvest)
# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    total_harvest = sum(num for row in harvest for num in row)
    return total_harvest


# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest):
    avg = [sum(row) / len(row) for row in harvest]
    return avg

# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))
