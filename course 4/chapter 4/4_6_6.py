"""4. Матрицы. Часть 3.
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив
её в соответствии с образцом.
"""
n = int(input())
matrix = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            matrix[i][j] = 1
        if i >= j and i >= n - 1 - j:
            matrix[i][j] = 1
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
