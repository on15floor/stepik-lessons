"""2. Повторяем основные конструкции языка Python. Часть 2.
На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
то есть, стоят вслед за меньшим числом.
"""
numbers = [int(n) for n in input().split()]
res = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        res += 1

print(res)
