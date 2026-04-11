# Количество корзин с овощами, шт.
baskets = 462
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(baskets, average_weight, price_per_kg):
    weight = baskets * average_weight
    price = weight * price_per_kg
    return weight, price

# Вызовите функцию calc() и обработайте вернувшееся значение.
total_weight, total_price = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {total_weight} кг. Оценённая стоимость урожая: {total_price}.')




'''example_str = 'Кабачки полезны для здоровья.'
# Напишите свой код здесь.
print(example_str[0])
print(example_str[10])
print(example_str[1])
print(example_str[-8])'''