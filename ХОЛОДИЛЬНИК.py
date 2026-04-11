from datetime import datetime, timedelta, date
from pprint import pprint
from decimal import Decimal


def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
    amount_decimal = Decimal(str(amount))
    batch = {'amount': amount_decimal, 'expiration_date': expiration_date}
    items.setdefault(title, []).append(batch)


def add_by_note(items, note):
    parts = note.split()
    if not parts:
        return

    # Проверка последняя часть дата
    last = parts[-1]
    try:
        # Парс как дату
        datetime.strptime(last, '%Y-%m-%d')
        # Если успешно – это дата
        expiration_date = last
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    except (ValueError, IndexError):
        # Если не дата или недостаточно частей – то даты нет
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    result = []
    needle_lower = needle.lower()
    for title in items:
        if needle_lower in title.lower():  # частичное совпадение
            result.append(title)
    return result


def get_amount(items, needle):
    # ищу все названия
    matching_titles = find(items, needle)
    total = Decimal(0)
    for title in matching_titles:
        for batch in items[title]:
            total += batch['amount']
    return total


def get_expired(items, in_advance_days=0):
    if in_advance_days is None:
        in_advance_days = 0
    current_date = date.today()
    target_date = current_date + timedelta(days=in_advance_days)
    result = {}
    for title, batches in items.items():
        total = Decimal(0)
        for batch in batches:
            exp_date = batch.get('expiration_date')
            if exp_date is not None and exp_date <= target_date:
                total += batch['amount']
        if total > 0:
            result[title] = total
    return list(result.items())


def print_stock(stock):
    # Вывод склада
    if not stock:
        print("Склад пуст.")
        return
    for title, batches in stock.items():
        print(f"  {title}:")
        for batch in batches:
            exp = batch['expiration_date']
            if exp is None:
                print(f"    amount={batch['amount']}, срок не указан")
            else:
                print(f"    amount={batch['amount']}, срок до {exp}")


# ининцал
stock = {}
goods_dict = {
    'Помидоры': 6.5,
    'Огурцы': 4.3,
    'Баклажаны': 2.8,
    'Перец': 2.2,
    'Капуста': 3.5
}

# ПРОВЕРКА
print('Начальное состояние склада')
print_stock(stock)

print('\nДобавление через add()')
add(stock, 'Помидоры', 2.5, '2025-12-31')
add(stock, 'Помидоры', 1.2, '2025-12-25')
print_stock(stock)

print('\nДобавление через add_by_note()')
add_by_note(stock, 'Яблоки 2.5 2026-05-01')
add_by_note(stock, 'Бананы 1.8')
add_by_note(stock, 'Салат Айсберг 0.9 2026-04-10')
add_by_note(stock, 'Перец сладкий 0.5 2026-04-05')
print_stock(stock)

print('\nТестирование find()')
for needle in ['помидоры', 'ПЕРЕЦ', 'салат', 'нет такого']:
    found = find(stock, needle)
    print(f'Поиск "{needle}": {found}')

print('\nТестирование get_amount()')
for needle in ['помидоры', 'перец', 'бананы']:
    total = get_amount(stock, needle)
    print(f'Общее количество {needle}: {total}')

print('\nТестирование get_expired()')
print('Товары, срок которых истёк (сегодня):')
expired_today = get_expired(stock)
if expired_today:
    for title, amount in expired_today:
        print(f'  {title}: amount={amount}')
else:
    print('Нет просроченных товаров.')

print(f'\nТовары, срок которых истекает в течение 7 дней (сегодня + 7 дней):')
expired_soon = get_expired(stock, in_advance_days=7)
if expired_soon:
    for title, amount in expired_soon:
        print(f'  {title}: amount={amount}')
else:
    print('Нет товаров с истекающим сроком.')

print('\nдобавление новых товаров')
add(stock, 'Новый товар', 3.14, '2026-12-31')
add(stock, 'Товар без срока', 10)
print_stock(stock)

print('\nПроверка обработки ошибок')
try:
    add(stock, 'Отрицательный товар', -5)
    print('Это не должно быть напечатано')
except ValueError as e:
    print(f'Ошибка (ожидаемо): {e}')
