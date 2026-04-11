from random import randint

# Начальная температура чая
current_temperature = 85

# Объявите цикл while
while current_temperature > 60:
    print('Прошла минута.')
    temperature = randint(1, 3)
    current_temperature = current_temperature - temperature
    print ('Чай остыл ещё на', temperature, '°C. Текущая температура:', current_temperature, '°C')
# В теле цикла получите случайное значение температуры, 
# на которое остыл чай в этой итерации (в диапазоне от 1 до 3).
# Уменьшите температуру чая на полученное значение.
# Напечатайте нужные сообщения.

# Напечатайте сообщение, которое должно быть выведено после завершения цикла.
print('Время пить чай')
