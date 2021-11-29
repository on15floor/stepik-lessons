"""4. Матрицы. Часть 1.
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит
след заданной квадратной матрицы.
"""
n = int(input())
matrix = []
total = 0

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    total += (matrix[i][i])

print(total)
