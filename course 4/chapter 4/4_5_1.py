"""4. Матрицы. Часть 2.
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.
"""
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(i * j)
    matrix.append(row)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
