"""4. Матрицы. Часть 1.
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
"""
n = int(input())
matrix = []

for _ in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
count = matrix[0][0]

for i in range(n):
    for j in range(n):
        if j <= i <= n-1-j:
            if matrix[i][j] > count:
                count = matrix[i][j]
        if j >= i >= n-1-j:
            if matrix[i][j] > count:
                count = matrix[i][j]
print(count)
