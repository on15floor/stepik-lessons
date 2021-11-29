"""4. Матрицы. Часть 2.
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.
"""
n = int(input())
matrix = [[int(item) for item in input().split()] for i in range(n)]

for l in range(n):
    for o in range(n-1, -1, -1):
        print(matrix[o][l], end=' ')
    print()
