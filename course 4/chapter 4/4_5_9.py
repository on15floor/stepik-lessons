"""4. Матрицы. Часть 2.
Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел 1,2,3,…,nˆ2 так,
что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.
"""
n = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(n)]
x = []
count = 0

for j in range(n):
    for i in range(n):
        x.append(matrix[j][i])

for j in range(1, ((n*n)+1)):
    if j in x:
        count += 1

if count == n*n:
    summa_diagomal = 0
    summa_diagomal1 = 0
    for i in range(n):
        summa_diagomal += matrix[i][i]
        summa_diagomal1 += matrix[i][n - i - 1]
    for i in range(n):
        bok_goriz = 0
        bok_vert = 0
        for j in range(n):
            bok_goriz += matrix[i][j]
            bok_vert += matrix[j][i]
    if bok_vert == bok_goriz == summa_diagomal == summa_diagomal1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
