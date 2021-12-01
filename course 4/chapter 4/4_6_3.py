"""4. Матрицы. Часть 3.
На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m и
заполняет её числами от 1 до n⋅m в соответствии с образцом.
"""
n, m = [int(i) for i in input().split()]
matrix = []

for i in range(n):
    row = []
    for j in range(m * i + 1, (m * (i + 1)) + 1):
        row.append(j)
    matrix.append(row)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
