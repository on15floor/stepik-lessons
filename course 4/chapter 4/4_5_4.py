"""4. Матрицы. Часть 2.
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
"""
n = int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]
res = 'YES'

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            res = 'NO'
print(res)
