"""2. Повторяем основные конструкции языка Python. Часть 2.
Напишите программу для определения, является ли число произведением двух чисел из данного набора,
выводящую результат в виде ответа «ДА» или «НЕТ».
"""


def some_func(num_list: list, num: int) -> str:
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            if i != j:
                if int(num_list[i]) * int(num_list[j]) == num:
                    return 'ДА'
    return 'НЕТ'


numbers = []
for i in range(0, int(input())):
    numbers.append(input())
div_num = int(input())
print(some_func(numbers, div_num))
