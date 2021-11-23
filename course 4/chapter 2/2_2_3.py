"""2. Повторяем основные конструкции языка Python. Часть 2.
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
Если в списке нечетное количество элементов, то последний остается на своем месте.
"""
numbers = [int(n) for n in input().split()]

res = []
for i in range(0, len(numbers), 2):
    if i == len(numbers) - 1:
        res.append(numbers[i])
    else:
        res.append(numbers[i+1])
        res.append(numbers[i])

print(' '.join(str(x) for x in res))
