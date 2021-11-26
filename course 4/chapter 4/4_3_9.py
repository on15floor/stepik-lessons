"""4. Вложенные списки. Вложенные списки. Часть 2.
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
"""
import math


def get_pascal_el(size: int, el_num: int) -> int:
    """Возвращает элемент треугольника паскаля"""
    return int(math.factorial(size) / (math.factorial(el_num) * math.factorial(size-el_num)))


def get_pascal_string(str_num: int) -> list:
    """Возвращает строку треугольника паскаля"""
    res = []
    for i in range(0, str_num + 1):
        res.append(get_pascal_el(str_num, i))
    return res


print(get_pascal_string(int(input())))
