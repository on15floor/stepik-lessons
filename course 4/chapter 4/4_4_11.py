"""4. Матрицы. Часть 1.
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших
среднего арифметического элементов данной строки.
"""
n = int(input())
matrix = []

for i in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)
