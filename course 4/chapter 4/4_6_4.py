"""4. Матрицы. Часть 3.
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив
её в соответствии с образцом.
"""
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = j*n+i+1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
