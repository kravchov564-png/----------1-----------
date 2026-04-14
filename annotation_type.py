"""Модуль для поиска максимального чётного числа в списке."""

from typing import List


def find_max_even_number(numbers: List[int]) -> int:
    """Ищет максимальное чётное значение в списке положительных целых чисел."""
    current_max = 0
    for _ in numbers:
        if _ % 2 == 0:
            current_max = max(_, current_max)
    return current_max


max_even = find_max_even_number([2, 12, 85, 0, 6])
print(f'Максимальное чётное число: {max_even}')
