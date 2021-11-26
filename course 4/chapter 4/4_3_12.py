"""4. Вложенные списки. Вложенные списки. Часть 2.
На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска),
а возвращает список из чанков указанной длины.
"""


def chunked(elements: list, num: int) -> list:
    res = []
    for i in range(0, len(elements), num):
        res.append(elements[i:num+i])
    return res


sss = input()
nnn = int(input())

print(chunked(sss.split(), nnn))
