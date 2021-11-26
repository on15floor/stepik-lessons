"""4. Вложенные списки. Вложенные списки. Часть 2.
На вход программе подается натуральное число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля.
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


n = int(input())
for i in range(0, n):
    print(' '.join(str(e) for e in get_pascal_string(i)))
