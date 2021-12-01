"""4. Матрицы. Часть 3.
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив
её в соответствии с образцом.
"""
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i+j) % m+1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
