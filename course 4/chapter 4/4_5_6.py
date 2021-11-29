"""4. Матрицы. Часть 2.
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
относительно горизонтальной оси симметрии.
"""
n = int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for o in range(n-1, -1, -1):
    for l in range(n):
        print(matrix[o][l], end=' ')
    print()
