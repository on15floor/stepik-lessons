"""4. Матрицы. Часть 3.
На вход программе подается натуральное число n. Напишите программу, которая создает матрицу размером n×n заполнив
её "спиралью" в соответствии с образцом.
"""
n, m = input().split()
n, m, x, y = int(n), int(m), 0, 0
matrix = [[0] * m for i in range(n)]

for i in range(1, n * m + 1):
    matrix[x][y] = i
    if x <= y and x + y < m - 1 and x <= (n - 1) / 2:
        y += 1
    elif x - y < n - m and x + y >= m - 1 and y >= (m - 1) / 2:
        x += 1
    elif x - y >= n - m and x + y > n - 1 and x >= (n - 1) / 2:
        y -= 1
    elif x > y + 1 and x + y <= n - 1 and y <= (m - 1) / 2:
        x -= 1
    else:
        y += 1

for i in matrix:
    for j in i:
        print(str(j).ljust(3), end='')
    print()
