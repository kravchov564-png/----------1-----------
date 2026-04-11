# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
from decimal import Decimal, getcontext
# Из модуля math импортируйте константу "пи".
from math import pi


# Установите необходимую точность для вычислений.
getcontext().prec = 10


# Функция get_ellipse_area() должна принимать два параметра:
# размер длинной и короткой полуоси.
def get_ellipse_area(long_axis, short_axis):
    # Вычислите площадь эллипса на основе переданных в функцию значений полуосей.
    # Верните получившееся значение (площадь эллипса).
    square_ellipse = pi * long_axis * short_axis
    return square_ellipse


# Приведите переменные к типу Decimal, помните, что Decimal() принимает строку.
pi = Decimal(str(pi)) # Значение "пи", тип Decimal
long_axis = Decimal('2.5') # Длинная полуось эллипса, тип Decimal.
short_axis = Decimal('1.75') # Короткая полуось эллипса, тип Decimal.
depth =  Decimal('0.35')# Глубина пруда, тип Decimal.

# Вызовите функцию get_ellipse_area(), в аргументах передайте длины полуосей эллипса.

# Результат работы функции присвойте переменной area:
area = get_ellipse_area(long_axis, short_axis)

# Вычислите объём пруда: умножьте площадь на глубину.
volume = area * depth

# Напечатайте фразы с результатами вычислений.
print(f'Площадь пруда: {area} кв.м.')
print(f'Количество воды для наполнения пруда: {volume} куб.м.')