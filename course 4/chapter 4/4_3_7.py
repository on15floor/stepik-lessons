"""4. Вложенные списки. Вложенные списки. Часть 2.
На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из
n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
"""

num = int(input())
res = [[j for j in range(1, num + 1)] for i in range(1, num + 1)]
for r in res:
    print(r)