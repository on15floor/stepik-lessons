"""4. Матрицы. Операции над матрицами.
Напишите программу для вычисления суммы двух матриц.
"""
n, m = [int(i) for i in input().split()]
matrix1 = list()
matrix2 = list()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix1.append(temp)
input()
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix2.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix1[i][j]+matrix2[i][j], end=' ')
    print()
