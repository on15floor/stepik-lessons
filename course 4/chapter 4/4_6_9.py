"""4. Матрицы. Часть 3.
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив
её "диагоналями" в соответствии с образцом.
"""
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
b = 0
count = 1

for i in range(n*m):
    b = i
    for j in range(n):
        for k in range(m):
            if k+j == b:
                matrix[j][k] = count
                count += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
