"""4. Матрицы. Часть 2.
Напишите программу, которая меняет местами столбцы в матрице.
"""
n, m = int(input()), int(input())
matrix = [input().split() for i in range(n)]
col1, col2 = [int(i) for i in input().split()]

for i in range(n):
    matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]

for row in matrix:
    print(*row)
