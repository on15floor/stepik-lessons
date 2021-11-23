"""2. Повторяем основные конструкции языка Python. Часть 2.
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их
в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует
слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник
заражен и нужно вывести номер холодильника, нумерация начинается с единицы
"""
import re

ref = []
for i in range(0, int(input())):
    ref.append(input())

res = []
for r in ref:
    if re.findall(r'\w*a\w*n\w*t\w*o\w*n\w*', r):
        res.append(ref.index(r) + 1)

print(*res)
